import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
names = ['California', 'Florida', 'Maryland', 'New York']
thedict = {}
for c in names:
    resp = requests.get(BASE_USAJOBS_URL, params = {'CountrySubdivision': c, 'NumberOfJobs': 1})
    thedict[c] = int(resp.json()['TotalJobs'])


print(thedict)
