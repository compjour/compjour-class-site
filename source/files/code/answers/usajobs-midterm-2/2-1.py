import json
import os
import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
CODES_URL = "http://stash.compjour.org/data/usajobs/CountryCode.json"
cdata = requests.get(CODES_URL).json()
mylist = []
for d in cdata['CountryCodes']:
    # getting non-US countries only
    if d['Code'] != 'US' and d['Value'] != 'Undefined':
        cname = d['Value']
        print("Getting:", cname)
        # we set NumberOfJobs to 1 because we don't need job listings, just
        # the TotalJobs
        atts = {'Country': cname,  'NumberOfJobs': 1}
        resp = requests.get(BASE_USAJOBS_URL, params = atts)
        data = resp.json()
        # the 'TotalJobs' value is always a string, we want it as an
        # int
        jobcount = int(data['TotalJobs'])
        mylist.append([cname, jobcount])

# save the file on to your hard drive
os.makedirs("data-hold", exist_ok = True)
f = open("data-hold/intl-jobcount.json", 'w')
f.write(json.dumps(mylist, indent = 2))
f.close()

