---
title: Reading the Metadata of Data Files in the Network Panel 
nav:
  part_of: intro-to-the-web-inspector
  prev: watching-traffic-network-panel
curriculum_order: 26

---

(Introduction writeup TK)


## Shake it up

In the [sandbox page](/files/pages/web-inspector/a/#shakes-sec), scroll down to the section tiled, [The Shakes](/files/pages/web-inspector/a/#shakes-sec). It looks something like this:

![img](/files/images/tutorials/devtools/the-shakes-page.png)

The data table and static Google Maps image display 4.5+ magnitude earthquake incidents from the [USGS Earthquake Hazards Program](http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php).


For the purposes of the sandbox page, I've __hard-coded__ the table and Google map (i.e. it's just part of the plain, static HTML) to show incidents in the data feed on __March 31__. If you wanted to scrape the table of this data, the Python code would look like this:

~~~py
import requests
import bs4
response = requests.get('http://www.compjour.org/files/pages/web-inspector/a')
soup = bs4.BeautifulSoup(response.text)
for row in soup.select('table#earthquakes tbody tr'):
    print(", ".join([cell.text for cell in row.select('td')]))
~~~


However, I've also created a JavaScript-powered button &ndash; "Shake the data" &ndash; to replace the table and Google Maps image with new HTML code that contains the up-to-the-minute data from the USGS. 


The JavaScript button works by fetching the [JSON file at this URL](http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson). 

But pretend didn't know that. You can use the Network Panel to see the data request that occurs when pressing the button. First, __clear__ the Network traffic panel so that it's empty. Then, __press the button__ (don't mind the shaking; that's just a JavaScript animation effect I threw in for kicks, not a direct result of retrieving data from the USGS):

![img](/files/images/tutorials/devtools/shakes-network-json.gif)

Two new GET requests are made by the browser, one to [earthquake.usgs.gov for the 4.5_day.geojson file](http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson) and the other to the [maps.googleapis.com/maps/api/staticmap endpoint](https://developers.google.com/maps/documentation/staticmaps/).


## The Network Resource Details Pane

You can view the [USGS 4.5_day.geojson file by pasting the URL directly in your browser's address bar](http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson). Or, you can view the details of the file by clicking on it, which will bring up the [Network Resource Details pane](https://developer.chrome.com/devtools/docs/network#network-resource-details).

In the Network Resource Details pane, the two most interesting tabs are __Headers__ and __Response__, which show, respectively, the details of the browser's request and the raw contents of the file. Clicking on the __x__ in the top-left corner of the pane returns you to the Network Panel's default traffic view:

![img](/files/images/tutorials/devtools/shakes-network-details-pane.gif)

### The Headers tab

The __Response__ tab is pretty straightforward, but the __Headers__ tab contains useful information about the __metadata exchanged between your browser and the USGS webserver_, so let's take a closer look at it:

![img](/files/images/tutorials/devtools/4_5_day.geojson.headers-tab.png)

The Headers tab contains several subsections of headers: __General__, __Response Headers__, and __Request Headers__. None of these are particularly exciting in this example, but it's worth noticing the kind of details that you learn about the USGS webserver, and what it learns about your browser. For example, in the Response headers, the USGS webserver tells us that it runs on `PHP/5.5.21` (according to the `X-Powered-By` property) and that the content it's sending  was `Last-Modified` at `Thu, 02 Apr 2015 23:03:17 GMT`. My browser, in the __Request Headers__, has told it that the referring address (i.e. where the request for data was initiated) is "http://www.compjour.org/files/pages/web-inspector/a/" and that my computer's operating system is `Mac OS X 10_10_2`.

__A sidenote:__ it's also worth noting that this __metadata can be faked__. Whoever wrote the USGS website code could've made up the `Last-Modified` date. And similarly, if I write a Python script to request the data, I could program it to have a `User-Agent` of `Web Browser From The FUTURE!`.


### Request/Response headers for a Google Map

The Static Google Maps request contains more interesting headers.

In the __Response Headers__ from Google, the `content-type` property tells our browser that the data is not text, but `image/png`; this is how the browser knows to render it as an image, rather than displaying it as raw binary text. And the `content-length` tells us that the image file itself is around 42,000 bytes:

![img](/files/images/tutorials/devtools/google-maps-response-headers.png)

#### Query String Parameters

The [Google Static Maps API](https://developers.google.com/maps/documentation/staticmaps/) works by reading a string of data parameters in the request URL. For example, to generate the following image:

![Google Map](/files/images/tutorials/devtools/google-staticmap-usgs-example.png){:style='max-width:500px'}



&ndash; this is the URL:

~~~
https://maps.googleapis.com/maps/api/staticmap?zoom=1&size=500x400&markers=size:tiny%7C-4.2721,143.1799&markers=size:tiny%7C-6.4291,146.9467&markers=size:tiny%7C38.6112,142.0651&markers=size:tiny%7C-35.5184,-98.7841&markers=size:tiny%7C-23.127,179.3652&markers=size:tiny%7C24.9652,145.9352&markers=size:tiny%7C6.5259,126.784&markers=size:tiny%7C-5.5064,152.6745&markers=size:tiny%7C-28.511,-71.1538&markers=size:tiny%7C-17.8368,-178.6629&markers=size:tiny%7C-4.5718,102.5482&markers=size:tiny%7C28.7119,86.3512&markers=size:tiny%7C14.8081,-91.454
~~~


This __Query String Parameters__ subpane contains a more user-friendly format of those URL parameters:

![img](/files/images/tutorials/devtools/google-maps-query-string.png)


These parameters are defined in [Google's documentation of the Static Maps API](https://developers.google.com/maps/documentation/staticmaps/#Usage). In the screencapture below, I show how the output of the Google Maps server changes as I add parameter key-value pairs to the URL (note that key-value pairs are separated by the __ampersand__ symbol, `&`):

- `size=600x100` (the `size` parameter is required)
- `zoom=6`
- `center=Stanford,CA`
- `maptype=hybrid`

![img](/files/images/tutorials/devtools/google-maps-static-parameters-gallery.png)



Learning all about the Hypertext Transfer Protocol (i.e. __HTTP__) is beyond the scope of this tutorial (here's the Wikipedia entry for the [Query string](http://en.wikipedia.org/wiki/Query_string)). However, it's worth knowing that when your browser makes a specific request for data -- via a direct URL or through a web form that you submit with a button -- a set of properties and values -- i.e. _data_ -- is sent to the server, in this case, Google Maps. And on that server is a program that reads those parameters and sends back the customized request. 

And with the Network Panel's __Resource Details Pane__ and __Headers tab__, we have an easy way to examine these parameters, which is very helpful when we skip using the browser and write our own scripts to access web resources.

