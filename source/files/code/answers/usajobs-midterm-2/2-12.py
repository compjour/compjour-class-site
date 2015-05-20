import json
import requests
import os
CA_FILE = 'data-hold/california.json'
if not os.path.exists(CA_FILE):
    print("Can't find", CA_FILE, "so fetching remote copy")
    resp = requests.get("http://stash.compjour.org/data/usajobs/california-all.json")
    f = open(CA_FILE, 'w')
    f.write(resp.text)
    f.close()

rawdata = open(CA_FILE).read()
jobs = json.loads(rawdata)['jobs']
## end job-loading code

def cleanmoney(val):
    x = val.replace('$', '').replace(',', '')
    return float(x)

def cleansalaryspread(job):
    return cleanmoney(job['SalaryMax']) - cleanmoney(job['SalaryMin'])

smalljobs = [job for job in jobs if cleanmoney(job['SalaryMax']) < 100000]
job = max(smalljobs, key = cleansalaryspread)
print('%s,%d,%d' % (job['JobTitle'], cleanmoney(job['SalaryMin']), cleanmoney(job['SalaryMax'])))









