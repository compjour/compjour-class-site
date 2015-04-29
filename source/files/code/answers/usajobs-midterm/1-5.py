import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
names = ['California', 'Florida', 'Maryland', 'New York']
thelist = []
for name in names:
    atts = {'CountrySubdivision': name, 'NumberOfJobs': 1}
    resp = requests.get(BASE_USAJOBS_URL, params = atts)
    jobcount = resp.json()['TotalJobs']
    thelist.append([name, jobcount])

print(thelist)
