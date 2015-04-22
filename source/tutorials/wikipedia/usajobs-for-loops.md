

~~~py
import requests
baseurl = "https://data.usajobs.gov/api/jobs"
states = ['California', 'Texas', 'Florida', 'Iowa']
for s in states:
    resp = requests.get(baseurl, params = {"CountrySubdivision": s})
    data = resp.json()
    print(s, "has", data['TotalJobs'], 'jobs.')
~~~






Iterating through a 





## Reimplementing max, sorted, and Counter



### Find the highest paid job


### Exercise 1: Find the most recently posted job






## Exercise 2: Get all the job objects in a given state

~~~py
import requests
jobs_list = []
state_url = "https://data.usajobs.gov/api/jobs"
atts = {"CountrySubdivision": "Iowa"}
atts['Page'] = 1
resp = requests.get(state_url, params = atts)
data = resp.json()
jobs = data['JobData']
jobs_list.extend(jobs)

# get page 2
atts['Page'] = 2
resp = requests.get(state_url, params = atts)
data = resp.json()
jobs = data['JobData']
jobs_list.extend(jobs)

# get page 3
atts['Page'] = 3
resp = requests.get(state_url, params = atts)
data = resp.json()
jobs = data['JobData']
jobs_list.extend(jobs)
~~~


#### Refactoring it as a loop

~~~py
import requests
def get_all_state_jobs(statename):
    jobs_list = []
    state_url = "https://data.usajobs.gov/api/jobs"
    atts = {"CountrySubdivision": statename, "Page": 1}
    resp = requests.get(state_url, params = atts)
    data = resp.json()
    jobs = data['JobData']
    jobs_list.extend(jobs)
    total_pages = int(data['Pages'])
    print("There are", total_pages, "total pages")

    for pgnum in range(2, total_pages + 1):
        print("On page", pgnum)
        atts['Page'] = pgnum
        resp = requests.get(state_url, params = atts)
        data = resp.json()
        jobs = data['JobData']
        jobs_list.extend(jobs)
    
    return jobs_list

~~~



## Exercise 3: Find the highest-paying job in any given state



