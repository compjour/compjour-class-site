---
title: Touring the USAJobs.gov Site and API
---

From its [About page](https://help.usajobs.gov/index.php/About_Us): 


> USAJOBS.gov is a free web-based job board enabling federal job seekers access to thousands of job opportunities across hundreds of federal agencies and organizations, allowing agencies to meet their legal obligation (5 USC 3327 and 5 USC 3330) of providing public notice for federal employment opportunities.

> As the Federal Government's official source for federal job listings and employment opportunity information, USAJOBS.gov provides a variety of opportunities. To date, USAJOBS has attracted over 17 million job seekers.

Sounds pretty spiffy,


Like [Craigslist](http://www.craigslist.org/), it's a site that has a tremendous amount of useful content and makes it easy to access, and yet we can think of ways that we [could remix the data](http://www.gregreda.com/2014/07/27/scraping-craigslist-for-tickets/) for our own needs. [Unlike Craigslist](https://gigaom.com/2013/08/19/craigslist-can-use-anti-hacking-law-to-stop-firm-from-scraping-its-data-court-rules/), USAJobs.gov encourages the reuse of its data and toward that end, [has created an API](https://data.usajobs.gov/):

> The target is to provide Public Jobs to Commercial Job Boards, Mobile Apps and Social Media. These consumers typically require a more lightweight data definition than typically presented on USAJOBS.


## The user-friendly website

Before we look at the API, it's best to explore the site as a typical web user.

The homepage is at [https://www.usajobs.gov/](https://www.usajobs.gov/). The user is presented with a couple of ways to customize the search: by __keyword__ and by __location__:

![img](/files/images/tutorials/usajobs-gov-homepage.png)


For this example, I'm going to [search for the location of __"Idaho"__](https://www.usajobs.gov/Search?Keyword=&Location=Idaho&search=Search&AutoCompleteSelected=false).


### Search results page

Notice where "Idaho" appears in the URL (I've omitted the `www.usajobs.gov` part for brevity):

[/Search?Keyword=&Location=Idaho&search=Search&AutoCompleteSelected=false](https://www.usajobs.gov/Search?Keyword=&Location=Idaho&search=Search&AutoCompleteSelected=false){:.rawurl}

This is what the [search results page looks like](https://www.usajobs.gov/Search?Keyword=&Location=Idaho&search=Search&AutoCompleteSelected=false):

![img](/files/images/tutorials/usajobs-gov-search-results.png)


Take a look at the left sidebar and the filtering features it provides, including the ability to set exclusion filters (by keyword, by staleness of posting):

![img](/files/images/tutorials/usajobs-gov-search-refine-sidebar.png){:.half}



### Job detail page


Each result has a details page; here's one for the job title of ["VMO (Public Health) (Supervisory Public Health Veterinarian)"](https://www.usajobs.gov/GetJob/ViewDetails/382487500)

[/GetJob/ViewDetails/382487500](https://www.usajobs.gov/GetJob/ViewDetails/382487500)

(Take note of the use of `382487500` as an identifier.)


![img](/files/images/tutorials/usajobs-gov-detailjob.png)

This particular position happens to be one not exclusive to Idaho, but is apparently hiring for as many as 511 different locations. It's not clear if each location needs just one veterinarian of if there are several veterinarian openings per city. One takeaway is that one job posting is replicated across several geographical regions; later on, as we attempt to download every job listing, it's somewhat-to-maybe-not-at-all relevant that job postings are not one-to-one with actual number of openings.

It's worth noticing the data points that are found in both the API and the website (job title, open period, pay scale and salary range). However, the version of the API that we'll use (the [REST-based API](https://data.usajobs.gov/Rest)) will be missing quite a few fields, notably the security clearance field and the wall of text for the job description (e.g. the Duties section and the degree requirements). The job detail webpage also has many features for logged-in users, such as being able to save and apply online to job listings; the REST API will not allow us to (easily) emulate such features.

## The developer-friendly API

Now that we've seen how the front-facing website works, let's see how its content is made accessible through an API. The homepage for the API lives at [data.usajobs.gov](https://data.usajobs.gov/), but we care specifically about the REST-based API: [data.usajobs.gov/Rest](https://data.usajobs.gov/Rest)




(Side note: The [SOAP-based API](https://data.usajobs.gov/Soap) has more data but is significantly more complicated to parse. Also, it's apparently marked for removal in May 2015. Another side-note, it's not important right now to know about [RESTful architectures](http://en.wikipedia.org/wiki/Representational_state_transfer); I simply use the term to distinguish between USAJobs.gov's offerings)





The most important section of the [REST-based API documentation](https://data.usajobs.gov/Rest) is under the tab titled __"API Query Parameters"__. But before digging through that, let's look at a sample URL:

[https://data.usajobs.gov/api/jobs?Title=Explosive](https://data.usajobs.gov/api/jobs?Title=Explosive)

If you visit that URL in your browser, you'll either see a glob of plaintext, like this:

![img](/files/images/tutorials/usajobs-gov-json-response-raw.png)


Or your browser might not attempt to render it all, and just download the file into your Downloads folder. Or you might see a basically empty file, because at the time you checked the API, there happen to be no jobs with "Explosive" in the title.

To see what I got, I saved a [cached version of the data that you can view here](http://stash.compjour.org/data/usajobs/title-explosive.json). I've stashed a copy [as a Github Gist, which may be easier to view](https://gist.github.com/dannguyen/236e7ad5d0da575f8718):

![img](/files/images/tutorials/usajobs-gov-json-as-a-gist.png)

### JSON for Humans

When it's properly formatted, [the JSON data format](http://en.wikipedia.org/wiki/JSON) is relatively easy to comprehend; indeed, it was designed as a way to send data as text that could be efficiently read by machines and humans alike. Even with knowing little about the format itself or the USAJobs API, you wouldn't be wrong in guessing that this data contains jobs that contain  the word "Explosive" in their `JobTitle` (e.g. `"AMMUNITION & EXPLOSIVES HANDLER"`) property. Or that when this search was made, 5 such jobs were open.

JSON is even more effective on the machine sideTK


## The Query String

The API's __base URL__ is: 

      https://data.usajobs.gov/api/jobs

Every query begins with this URL, though visiting it as is returns an empty response.

To get results, add a __parameter__, which is expressed as a __key__-__value__ (or sometimes referred to as _field-value_) pair. In the example below, `title` is the __key__ and `director` is the __value__; the __equals sign__ is used to connect the key to its value:

        title=director

 Append this parameter to the base URL, and you'll get results for all open positions with `director` in the title. Note that the __question mark__ is used to separate the __base URL__ from its __query string__, i.e. its list of __parameters__:

[https://data.usajobs.gov/api/jobs?title=director](https://data.usajobs.gov/api/jobs?title=director){:.rawurl}

#### Multiple parameters

If you want find jobs in the state of __Nevada__, you can either use the key/field of __CountrySubdivision__, or the more broad `LocationName` (which would presumably include jobs in _Nevada City, California_). To find __director__ positions in the state of __Nevada__, you combine the two key-value pairs using an __ampersand__ as a __delimiter__:

[https://data.usajobs.gov/api/jobs?title=director&CountrySubdivision=Nevada](https://data.usajobs.gov/api/jobs?title=director&CountrySubdivision=Nevada)

You can find the entire list of possible parameters in the [REST API documentation](https://data.usajobs.gov/Rest), under the __API Query Parameters__ tab.

The keys/fields most important to us are:

- `Page` - a broad search can return as many as 5,000 results. By default, the API returns 25 results at a time. Increasing the `Page` parameter allows us to get through all of the listings.
- `NumberOfJobs` - by default, this is set to a value of **25** but can be increased to a maximum of **250**, reducing the number of pages (i.e. URL requests) by a factor of 10.
- `CountrySubdivision` - This is used to specify a U.S. state by name. Currently, it does not support provinces/states in other countries, e.g. Ontario, Canada. A list of possible values can be found at [schemas.usajobs.gov/Enumerations/CountrySubdivision.xml](https://schemas.usajobs.gov/Enumerations/CountrySubdivision.xml)
- `Country` - This is used to specify a country by name. A list of possible countries can be found at [schemas.usajobs.gov/Enumerations/CountryCode.xml](https://schemas.usajobs.gov/Enumerations/CountryCode.xml). Apparently these are used elsewhere in the U.S. government, such [as the IRS](http://www.irs.gov/Tax-Professionals/e-File-Providers-&-Partners/Foreign-Country-Code-Listing-for-Modernized-e-File), which will cause us a huge inconvenience when we try to mix with systems (such as Google Charts) that use ISO codes.
- `Series` - A 4-digit number used by the federal government to categorize jobs, e.g. [1000 - 1099 is designated for Information and Arts](http://www.opm.gov/policy-data-oversight/classification-qualifications/general-schedule-qualification-standards/#url=1000-ndx), with 1015 being designated for [Museum Curator](http://www.opm.gov/policy-data-oversight/classification-qualifications/general-schedule-qualification-standards/1000/museum-curator-series-1015/) positions.
- `OrganizationID` - Can be used to specify an organization, such as `HE` for the Department of Health and Human Services, or more specifically, `HE39` for the Centers for Disease Control and Prevention. A list of codes Agency codes [can be found here](https://schemas.usajobs.gov/Enumerations/AgencySubElement.xml).

All other fields are less important for our data-gathering purposes. For example, it's harder to enumerate all the possible values for the `Title`, `Keyword`, and `LocationName` fields, though those would be useful if you were to build a service that passed along users' queries to the data.usajobs.gov API.


#### Limitations

While the API is fairly flexible, it doesn't appear to let us do queries with multiple values per field (i.e. return jobs in France _and_ Germany) or other kinds of logical combinations (e.g. get jobs with _this_ keyword but __not__ _that_ keyword). 

This limitation isn't a big deal because with programming, we can automate the collection of all the data. However, it's not as straightforward as just hitting up the system and iterating across 1,000 pages. Do a search for job listings using __United States__ as the __Country__ (quick note: URLs do not allow certain characters, such as space characters, hence, the __plus sign__):

[https://data.usajobs.gov/api/jobs?Country=United+States](https://data.usajobs.gov/api/jobs?Country=United+States)

The result will look something like:

![img](/files/images/tutorials/data-usajobs-gov-country-us-5000.png)

Are there exactly 5,000 job openings in the United States? Could be. But more likely, it's that there are _more_ than 5,000 but the API will only return a maximum of 5,000 results &ndash; altering the `NumberOfJobs` parameter won't change that ceiling: 

[https://data.usajobs.gov/api/jobs?Country=United+States&NumberOfJobs=250](https://data.usajobs.gov/api/jobs?Country=United+States&NumberOfJobs=250){:.rawurl}


Thus, to get _all job listings for the U.S._, we will have to provide at least one other parameter, such as `CountrySubdivision`, and then iterate over all possible values, e.g. all 50 states and D.C. (actually, we can take out the `Country` parameter, since these subdivisions are by definition inside the U.S.)And of course, some of these individual states will have more than `250` listings, which will require adding the `Page` parameter. So if the state of __California__ has 700 job openings, three separate API requests are necessary:

[https://data.usajobs.gov/api/jobs?CountrySubdivision=California&NumberOfJobs=250](https://data.usajobs.gov/api/jobs?CountrySubdivision=California&NumberOfJobs=250){:.rawurl}

[https://data.usajobs.gov/api/jobs?CountrySubdivision=California&NumberOfJobs=250&Page=2](https://data.usajobs.gov/api/jobs?CountrySubdivision=California&NumberOfJobs=250&Page=2){:.rawurl}

[https://data.usajobs.gov/api/jobs?CountrySubdivision=California&NumberOfJobs=250&Page=3](https://data.usajobs.gov/api/jobs?CountrySubdivision=California&NumberOfJobs=250&Page=3){:.rawurl}


## Play with Python

Let's briefly do what we've just done &ndash; accessing the API via browser &ndash; except via Python code. Don't worry if you don't understand most of it; just focus on the parts you _do_ recognize. You can run this in __iPython__:

To download the first 25 job openings in California:

~~~py
import requests
resp = requests.get("https://data.usajobs.gov/api/jobs?CountrySubdivision=California")
# at this point, download has completed, now convert it
# to a data structure
data = resp.json()
print("Total jobs:", data['TotalJobs'])
jobs = data['JobData']
print("First job title:", jobs[0]['JobTitle'])
~~~

The result should look something like (but not exactly):

~~~
Total jobs: 760
First job title: Automotive Mechanic Supervisor
~~~

And here's a preview of how writing all that code (eventually) allows us to easily increase the scope of our task:

~~~py
import requests
baseurl = 'https://data.usajobs.gov/api/jobs?CountrySubdivision='
states = ['California', 'Texas', 'Nevada', 'Oregon', 'Maine', 'Iowa']
for s in states:
    resp = requests.get(baseurl + s)
    data = resp.json()
    print("For state", s)
    print("  Total jobs:", data['TotalJobs'])
    jobs = data['JobData']
    print("  First job title:", jobs[0]['JobTitle'])
~~~

Result:

~~~
For state California
  Total jobs: 760
  First job title: Automotive Mechanic Supervisor
For state Texas
  Total jobs: 654
  First job title: INTERDISCIPLINARY ENGINEER
For state Nevada
  Total jobs: 199
  First job title: Public Health Advisor (French)
For state Oregon
  Total jobs: 249
  First job title: Public Health Advisor (French)
For state Maine
  Total jobs: 58
  First job title: Public Health Advisor (French)
For state Iowa
  Total jobs: 74
  First job title: Licensed Practical Nurse - Primary Care Clinic
~~~

Hopefully you can see how this can be expanded to all 50 states, or all 190+ countries and territories.






