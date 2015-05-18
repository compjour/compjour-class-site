## Dollars for Docs

_Note: I produced [this for ProPublica in 2010](http://projects.propublica.org/docdollars)._


## Quick pitch

Find out how much Big Pharma pays your doctor.

## The old way, step-by-step

To find out if a particular physician has any kind of financial relationship with a pharmaceutical company:

1. Think of a physician's name.
2. Think of a drug company's name.
3. Find out if drug company has publicly disclosed its financial relationships with doctors.
4. Find the site/document in which these disclosures have been made.
5. Do a manual search for the physician's name.


## The new way, step-by-step

1. Go to my website
2. Think of a physician's name
3. Type in the name into a search box
4. Read the results


## Data details

### Where does the data come from? How is it collected?

The data comes from drug companies themselves, posted online, usually as part of a settlement with the Justice Department. Here's an [example with Pfizer](http://www.justice.gov/opa/pr/justice-department-announces-largest-health-care-fraud-settlement-its-history):

> "This historic settlement emphasizes the government’s commitment to corporate and individual accountability and to transparency throughout the pharmaceutical industry," said Daniel R. Levinson, Inspector General of the United States Department of Health and Human Services. "The corporate integrity agreement requires senior Pfizer executives and board members to complete annual compliance certifications and opens Pfizer to more public scrutiny by requiring it to make detailed disclosures on its Web site. We expect this agreement to increase integrity in the marketing of pharmaceuticals."

Here's Pfizer's website of [Payments to Health Care Professionals](http://www.pfizer.com/responsibility/working_with_hcp/payments_report).

### What data-cleaning/processing needs to be done?

Each company has a different way of posting their data; Pfizer's will require web-scraping, for example ([Data on Fees to Doctors Is Called Hard to Parse -  (nytimes.com)](http://www.nytimes.com/2010/04/13/business/13docpay.html?_r=0) 
). Others, [such as GlaxoSmithKline, come in PDFs](http://fortherecord.payments.us.gsk.com/hcppayments/archive.html), and so the PDFs need to be converted to text and then parsed into data in a painful, manual way.

Also, since each drug company has its own data system, they often refer to doctors with similar but not exact-matching names (e.g. Robert J. Smith and Bobby Johnson Smith). And each company is required to disclose different periods of times and different kinds of data, so not everything is apples-to-apples.


## Implementation details

### Describe the public-facing endpoints

The [front page](http://projects.propublica.org/docdollars/) will contain a big search box to let users type in their doctors' names. The search results page will contain a table, with these fields: doctor name, year, city/state, drug company, category of relationship (i.e. research, consulting, promotion).

Each result will be clickable/linkable and have its own detailed page showing more about the payment, even those most payment records don't have much information. But we need to include a lot of explanatory material and context, such as what these payments mean or don't mean (i.e. they _don't_ mean that the doctor is corrupt).

I will also have views that will list all records by __state__ and by __company__, so that users can easily see which doctors in their state have the largest financial relationship. Or, to see which companies pay the most to doctors.


### How will the data be stored?

I'll store all the raw data files (PDFs, HTML pages, etc) on a backup disk, just so I can refer to the source material if anyone disputes a listing. However, the site (which will be Ruby on Rails) will run off of a MySQL database.

## Who else has done it and how is your attempt better?

Each of the drug companies have "done it", but their records listings all have shortcomings. Pfizer's site, for example, [makes it all but impossible to do anything else besides a specific names search](http://www.nytimes.com/2010/04/13/business/13docpay.html?_r=0), which blocks interesting inquiries such as finding the doctors who receive the most money from them.


## Pre-mortem

- __Too difficult to gather the data__ - Scraping HTML and PDFs is very time-consuming work and requires studying each site/document and understanding its particular structure.
- __Too difficult to avoid errors__ - Having the wrong records associated with the wrong doctors is something that could easily happen given the complexity of reverse-engineering the data files.
- __Data is inherently limited__ - The companies all disclose different categories and time periods, and so it requires a lot of study to make sure that we're correctly categorizing things (such as honorariums and money given for doing presentations, versus doing research).
- __Database crashes__ - There's a lot of records, and if people do a lot of searches, the app could crash.





