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

[/Search?Keyword=&Location=Idaho&search=Search&AutoCompleteSelected=false](https://www.usajobs.gov/Search?Keyword=&Location=Idaho&search=Search&AutoCompleteSelected=false)

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













Ideally, the website itself would use the API as a means of fetching and delivering data &ndash; this is called [dogfooding](http://en.wikipedia.org/wiki/Eating_your_own_dog_food), as in, "eat your own dog food". It's hard to tell if that's going on here, as there are fewer ways to search the API compared to the website's [advanced search](https://www.usajobs.gov/Search/AdvancedSearch). And the form of the API we're using, the REST JSON, doesn't have all of the fields.






