


## I Heart New York Museums

_Note: This is something I built many years ago: [http://iheartnymuseums.com/](http://iheartnymuseums.com/)_

## Quick pitch

A complete list of when New York museums and galleries are free and open.

## The old way

To find when a New York museum is free and open, someone must:

1. Think of a museum
2. Find that museum's webpage
3. Find the hours of operation
4. Find the admissions info
5. Figure out if the free day/hours matches their schedule
6. Look up directions to the museum

## The new way

1. They visit my webpage
2. They select the day of the week they're interested in to see the museum list sorted by number of free hours that day
3. They see which of those museums they want to go to
4. They look on my interactive map to find where the museum is located


## Data details

### Where does the data come from? How is it collected?

I have to think up a list of museums myself, and then find (via Google) and visit the webpage of each one manually and record the operation/free hours and addresses in a spreadsheet. The geo-coordinates come from Google's Geocoding API.

### What data-cleaning/processing needs to be done?

Most of the data I want is just hand-entered by whoever designed each museum's webpage. So I have to manually enter it into a spreadsheet. I'll make a column for each day of the week (e.g. Sunday, Monday, Tuesday). Then 


## Implementation details

### Describe the public-facing endpoints

This is a one-page app. The user goes to this page and clicks on the interactive-sortable table headers. Or, the user can look at the interactive map and click on markers of geographical interest.

### How will the data be stored?

The data will remain in the Google Spreadsheet. I'll write a script that reads directly from that spreadsheet and produces the HTML. I'll have to run that script manually but that's OK since museum hours do not change very often.

## Who else has done it and how is your attempt better?

- [Timeout New York](http://www.timeout.com/newyork/museums/free-museum-days-in-nyc-cultural-center) - I will have more museums and my list will be easier to skim across the weekdays, whereas TONY requires users to scroll through long blocks of prose.

- [FreeMuseumDay.org](http://freemuseumday.org/nyc.html) - The non-tabular format means you basically have to read each line of tiny-font to see which museums are relevant to the weekday you care about.

## Pre-mortem

- __Too much data-entry:__ There are a lot of museums in New York and doing data-entry for all of them could drive me insane.
- __Too much data for a single-page design:__ The number of museums will make the site very long and unwieldy to scroll through. Without a lot of UI/UX magic, the site will require users to do a lot of work to just skim the list.
- __Frequent changes:__ Even though any single museum may not change its operating/free hours very often, with more than 100+ museums, it's possible that at least a few changes will have to be made on at least a semi-annual basis. And I have no way to auto-detect such changes, particularly single-day closures, which means some users will be misled by my information.


