import requests
from urllib.parse import urljoin
import bs4

# first, download the news home page at:
# http://news.stanford.edu/news/
home_url = "http://news.stanford.edu/news/"
home_page = requests.get(home_url).text
home_soup = bs4.BeautifulSoup(home_page)
# Then, get the list of topics
topic_links = home_soup.select('.topiclist li a')
print("There are {} topic links total".format(len(topic_links)))

# for each topic link, download the page, and print the first (i.e. latest)
# headline
for link in topic_links:
    # we only want URLs that have /tags as part of the URL
    if link['href'].find('/tags') > -1:
        print("Tagged topic:", link.text, "at URL:", link['href'])
        tag_url = urljoin(home_url, link['href'])
        # now fetch the topic page
        # notice how it's basically the same pattern as the first call
        tpage = requests.get(tag_url).text
        tsoup = bs4.BeautifulSoup(tpage)
        heds = tsoup.select("#main-content .postcard-text")
        # getting the first member of the list
        h = heds[0]
#        dateline = h.find('.dateline').text
        hed = h.find('h3').text
        print("   Latest headline: {}".format(hed))
        print("")
