import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
resp = requests.get(BASE_USAJOBS_URL, params = {"CountrySubdivision": 'California', 'NumberOfJobs': 250})
data = resp.json()

my_dict = {}
for job in data['JobData']:
    orgname = job['OrganizationName']
    if my_dict.get(orgname):
        my_dict[orgname] += 1
    else:
        my_dict[orgname] = 1

print(mydict)
