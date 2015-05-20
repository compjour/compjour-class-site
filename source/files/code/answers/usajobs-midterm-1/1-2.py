import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
atts = {"CountrySubdivision": 'Alaska', 'NumberOfJobs': 1}
ak_resp = requests.get(BASE_USAJOBS_URL, params = atts)
ak_data = ak_resp.json()

atts = {"CountrySubdivision": 'Hawaii', 'NumberOfJobs': 1}
ha_resp = requests.get(BASE_USAJOBS_URL, params = atts)
ha_data = ha_resp.json()

print("Alaska has %s job listings." % ak_data['TotalJobs'])
print("Hawaii has %s job listings." % ha_data['TotalJobs'])
t = int(ak_data['TotalJobs']) + int(ha_data['TotalJobs'])
print("Together, they have %s total job listings." % t)
