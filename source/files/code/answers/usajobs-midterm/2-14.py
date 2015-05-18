import json
import requests
import os
from collections import Counter
from operator import itemgetter
CA_FILE = 'data-hold/california.json'
if not os.path.exists(CA_FILE):
    print("Can't find", CA_FILE, "so fetching remote copy")
    resp = requests.get("http://stash.compjour.org/data/usajobs/california-all.json")
    f = open(CA_FILE, 'w')
    f.write(resp.text)
    f.close()
rawdata = open(CA_FILE).read()
jdata = json.loads(rawdata)
jobs = jdata['jobs']



def get_ca_cities(job):
    cities = [c for c in job['Locations'].split(';') if 'California' in c]
    return [c.split(',')[0] for c in cities]

cityjobs = []
for job in jobs:
    cityjobs.extend(get_ca_cities(job))

citylist = list(Counter(cityjobs).items())
# convert those tuples into lists
citylist = [list(t) for t in citylist]
# and then sort it by jobcount
chartdata = [['City', 'Jobs']]
chartdata.extend( citylist )


#####
# now create tablerows
sortedlist = sorted(citylist, key = itemgetter(1), reverse = True)
tablerows = []
for d in sortedlist:
    tablerows.append("<tr><td>%s</td><td>%s</td></tr>" % (d[0], d[1]))
tablerows = "\n".join(tablerows)




outs =  open("2-14.html", "w")
## assumes you've made a copy of this file
# http://stash.compjour.org/files/code/answers/usajobs-midterm/sample-geochart-cities.html
# and stashed it at a relative path:
# sample-geochart-cities.html
with open("sample-geochart-cities.html") as f:
    htmlstr = f.read()
    htmlstr = htmlstr.replace('#CHART_DATA#', str(chartdata))
    htmlstr = htmlstr.replace('#TABLE_ROWS#', tablerows)
    outs.write(htmlstr)

outs.close()
