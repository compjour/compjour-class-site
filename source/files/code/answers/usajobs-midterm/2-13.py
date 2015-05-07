import json
import requests
import os
from datetime import datetime
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

collection_date = datetime.strptime(jdata['date_collected'], '%Y-%m-%dT%H:%M:%S')

## end job-loading code

def daysonlist(job):
    postdate = datetime.strptime(job['StartDate'], '%m/%d/%Y')
    return (collection_date - postdate ).days


for job in sorted(jobs, key = daysonlist):
    days = daysonlist(job)
    if days <= 2:
        print('%s,%s,%s' % (job['JobTitle'], days, job['ApplyOnlineURL']))

