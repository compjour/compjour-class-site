import pandas as pd

# scraping stanford's tuition page
from lxml import html
import requests
import re
# live site is at: "http://facts.stanford.edu/administration/finances"
url = 'http://stash.compjour.org/mirrors/facts.stanford.edu/administration/finances.html'
resp = requests.get(url)
doc = html.fromstring(resp.text)
table = doc.cssselect('table')[3]

rows = []
for trs in table.cssselect('tr')[1:]:
    yr, cost = [t.text for t in trs]
    rows.append( [int(yr.split('-')[0]), int(re.sub('\D', '', cost))])


# alternatively
# rows = [( int(tds[0].text.split('-')[0]), int(re.sub('\D', '', tds[1].text))) for tds in
#              [trs for trs in table.cssselect('tr')[1:]]]


