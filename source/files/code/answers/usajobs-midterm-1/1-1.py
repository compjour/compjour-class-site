import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
state_name = 'New York'
atts = {"CountrySubdivision": state_name, 'NumberOfJobs': 1}
resp = requests.get(BASE_USAJOBS_URL, params = atts)
data = resp.json()
print("%s has %s job listings." % (state_name, data['TotalJobs']))
