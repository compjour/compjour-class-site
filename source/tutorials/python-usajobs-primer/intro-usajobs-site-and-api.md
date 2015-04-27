---
title: Touring the USAJobs.gov Site and API
---



From its [About page](https://help.usajobs.gov/index.php/About_Us): 


> USAJOBS.gov is a free web-based job board enabling federal job seekers access to thousands of job opportunities across hundreds of federal agencies and organizations, allowing agencies to meet their legal obligation (5 USC 3327 and 5 USC 3330) of providing public notice for federal employment opportunities.

> As the Federal Government's official source for federal job listings and employment opportunity information, USAJOBS.gov provides a variety of opportunities. To date, USAJOBS has attracted over 17 million job seekers.

Sounds pretty spiffy,


Like [Craigslist](http://www.craigslist.org/), it's a site that has a tremendous amount of useful content and makes it easy to access, and yet we can think of ways that we [could remix the data](http://www.gregreda.com/2014/07/27/scraping-craigslist-for-tickets/) for our own needs. [Unlike Craigslist](https://gigaom.com/2013/08/19/craigslist-can-use-anti-hacking-law-to-stop-firm-from-scraping-its-data-court-rules/), USAJobs.gov encourages the reuse of its data and toward that end, [has created an API](https://data.usajobs.gov/):

> The target is to provide Public Jobs to Commercial Job Boards, Mobile Apps and Social Media. These consumers typically require a more lightweight data definition than typically presented on USAJOBS.


## Using the website

Before we look at the API, it's best to explore the site as a typical web user.

The homepage is at [https://www.usajobs.gov/](https://www.usajobs.gov/). The user is presented with a couple of ways to customize the search: by __keyword__ and by __location__:

![img](/files/images/tutorials/usajobs-gov-homepage.png)


For this example, I'm going to [search for the location of __"Idaho"__](https://www.usajobs.gov/Search?Keyword=&Location=Idaho&search=Search&AutoCompleteSelected=false).

Check out how that affects the URL (I've omitted the `www.usajobs.gov` part for brevity):

[/Search?Keyword=&Location=Idaho&search=Search&AutoCompleteSelected=false](https://www.usajobs.gov/Search?Keyword=&Location=Idaho&search=Search&AutoCompleteSelected=false)

This is what the [search results page looks like](https://www.usajobs.gov/Search?Keyword=&Location=Idaho&search=Search&AutoCompleteSelected=false):



