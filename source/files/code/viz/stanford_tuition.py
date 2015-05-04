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
tuition_rows = []
for row in rows:
    if len(tuition_rows) == 0:
        pass
    else:
        lastyr, lastcost = tuition_rows[-1]
        tuition_rows.extend([[lastyr + i, lastcost] for i in range(1, row[0] - lastyr)])
    tuition_rows.append(row)

tuition_df = pd.DataFrame(tuition_rows, columns = ['year', 'tuition'])

########################
# Set up inflation calculator

import csv
import requests
url = 'https://raw.githubusercontent.com/datasets/cpi-us/master/data/cpiai.csv'
cpidata = list(csv.reader(requests.get(url).text.splitlines()))
cpidf = pd.DataFrame(cpidata[1:], columns = cpidata[0])
cpidf = pd.DataFrame.convert_objects(cpidf, convert_dates = 'coerce', convert_numeric = True)
cpimean_df = cpidf.groupby(cpidf['Date'].map(lambda x: x.year)).mean()

def adjust_for_inflation(amt, from_year, to_year):
    cpimean_df['Index'][to_year] / cpimean_df['Index'][from_year]
    return round(ratio * amt, 2)



### Now let's graph things
import matplotlib.pyplot as pyplot

# Without inflation
pyplot.plot(tuition_df['year'], tuition_df['tuition'])

# Adjusted for 2014 dollars
tuition_df['adjusted_tuition'] = tuition_df.apply(lambda x: adjust_for_inflation(x['tuition'], x['year'], 2014), axis=1)


# Make a line graph
pyplot.plot(tuition_df['year'], tuition_df['tuition'])
pyplot.plot(tuition_df['year'], tuition_df['adjusted_tuition'])

# Make a bar chart
pyplot.bar(tuition_df['year'], tuition_df['tuition'])
pyplot.bar(tuition_df['year'], tuition_df['adjusted_tuition'])



########### change

tuition_df['tuition_pct_yoy'] = tuition_df.pct_change()['tuition'] * 100
tuition_df['adjusted_tuition_pct_yoy'] = tuition_df.pct_change()['adjusted_tuition'] * 100
cpisum_df = cpidf.groupby(cpidf['Date'].map(lambda x: x.year)).sum()

pyplot.bar(tuition_df['year'], tuition_df['adjusted_tuition_pct_yoy'])
pyplot.bar(cpisum_df.index, cpisum_df['Inflation'])
