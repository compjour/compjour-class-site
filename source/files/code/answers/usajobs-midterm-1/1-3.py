import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
countries = ['China', 'South Africa', 'Tajikistan']
total_jobs = 0
for cname in countries:
    atts = {'Country': cname,  'NumberOfJobs': 1}
    resp = requests.get(BASE_USAJOBS_URL, params = atts)
    tjobs = int(resp.json()['TotalJobs'])
    print("%s currently has %s job listings.." % (cname, tjobs))
    total_jobs += tjobs

print("Together, they have %s total job listings." % total_jobs)

