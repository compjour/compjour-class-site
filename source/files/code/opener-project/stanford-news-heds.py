fname = 'stuff/news.stanford.edu.html'
f = open(fname).read()

import bs4
soup = bs4.BeautifulSoup(f)
a_string = "The currently downloaded {fname} has {h_count} recent headlines and {img_count} images"
hc = len(soup.select('#more-news h3'))
ic = len(soup.select('img'))
print(a_string.format(fname = fname, h_count = hc, img_count = ic))

if hc > ic:
    print("There are more headlines")
else:
    print("There are more images")

# alternatively:
# print(a_string.format(
#     fname = fname,
#     h_count = len(soup.select('#more-news h3')),
#     img_count = len(soup.select('img'))
# ))
