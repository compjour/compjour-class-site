import json
import os
import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
STATECODES_URL = "http://stash.compjour.org/data/usajobs/us-statecodes.json"
names = requests.get(STATECODES_URL).json()
mylist = []
for name in names.keys():
    print("Getting:", name)
    resp = requests.get(BASE_USAJOBS_URL, params = {'CountrySubdivision': name, 'NumberOfJobs': 1})
    jobcount = int(resp.json()['TotalJobs'])
    mylist.append([name, jobcount])

os.makedirs("data-hold", exist_ok = True)
f = open("data-hold/domestic-jobcount.json", 'w')
f.write(json.dumps(mylist, indent = 2))
f.close()
