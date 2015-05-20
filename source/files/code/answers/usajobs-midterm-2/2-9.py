import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
resp = requests.get(BASE_USAJOBS_URL, params = {"CountrySubdivision": 'California', 'NumberOfJobs': 250})
data = resp.json()

mydict = {'Full-time': 0, 'Other': 0}
for job in data['JobData']:
    if 'full' in job['WorkSchedule'].lower():
        mydict['Full-time'] += 1
    else:
        mydict['Other'] += 1

print(mydict)
