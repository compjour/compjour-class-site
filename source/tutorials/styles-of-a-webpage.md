---
title: The Styles of a Webpage
curriculum_order: 12

nav:
  prev: elements-of-a-webpage
  next: watching-traffic-network-panel
  part_of: intro-to-the-web-inspector 
---


In the previous lesson, I advised you not to spend too much time trying to memorize HTML tags and attributes. Part of this is because it's easier just to learn as you go in tandem with the DevTools inspector. And part of it is because HTML tags themselves &ndash; whether it's `<em>` for _italicized text_, `<b>` for __bold___, or even `<small>` for <small>reduced-size font</small> &ndash; do not actually describe what their corresponding elements will look like in the browser.

Instead, web browsers use _another_ language, referred to as __CSS__, short for [Cascading Style Sheets](http://en.wikipedia.org/wiki/Cascading_Style_Sheets), to determine the visual appearance of HTML elements.

I'll repeat my previous advice: it's not worth memorizing the _expansive syntax_ (CSS is a language, after all). But it is worth knowing the concept, and how to interactively explore and debug it with the Chrome DevTools.

Knowing about CSS isn't particularly essential for the data-programming domain, but it is extremely essential if you intend on publishing any kind of webpage. 

And for web-scraping tasks, the concept of __CSS selectors__ will be an important takeaway from this lesson.


## Introduction to CSS

The CSS syntax, in general, looks something like this:

~~~css
some_selector{
  some-visual-property: the-value;
  another-visual-property: another-value;
}
~~~

The following snippet would render `h1` elements (`h1` is the tag used for a top-level __headline__) as <span style="color: #090;">green</span>, _italicized_ text using the [Comic Sans font](http://en.wikipedia.org/wiki/Comic_Sans:

~~~css
h1{
  color: green;
  font-family: "Comic Sans MS";
  font-style: italic;
}
~~~

In the snippet above:

- `h1` is the __selector__
- `color`, `font-family`, and `font-style` are the __properties__
- `green`, `"Comic Sans MS"`, and `italic` are the respective __values__ for the given properties


### External stylesheets

This style code is usually saved in another file (referred to as an _external stylesheet_), and a webpage can tell the browser to include that stylesheet via this bit of HTML:

~~~html
<link rel="stylesheet" href="/path/to/those-styles.css">
~~~


There's a lot more to CSS, including what the _Cascading_ part means. For now, it's enough to know that when it comes to web pages, there's a whole other language for defining the look of HTML elements on a page. The fact that these _styles_ can be defined in external files means that there is a _separation of concerns_, specifically, separating the __content__ of a webpage (the text, the multimedia) from its __presentation__.

This _separation of concerns_ is an important concept in all kinds of programming, and the use of CSS is one of the best real-world examples of how it works. So let's dive into a little CSS using the Chrome DevTools.

For this lesson, we'll be using the test page at this URL:

[http://www.compjour.org/files/pages/web-inspector/inline/](/files/pages/web-inspector/inline/)


## The Styles Pane

As we learned in the previous lesson, the __Elements__ panel can be opened up by __right-clicking__ on any HTML element and selecting __Inspect Element__.


The __Styles Pane__ is the _right_-half of the __Elements__ panel. I usually resize the panel so that the __DOM Tree Pane__ takes up 60% of the overall panel, as HTML code tends to be longer in line-length than the style code:

![img](/files/images/tutorials/devtools/style-pane-resize.gif)



As you click through the HTML elements on the left pane, notice how the right pane changes. 

![img](/files/images/tutorials/devtools/style-clicking-selectors.gif)


### Inline CSS

Clicking on the `<body>` element reveals a list of style codes that affect the  `<body>` element's visual presentation. The top-most style states that the specific element (i.e. `element.style`) has a `padding` value of `50px`, i.e. the browser is instructed to put `50px` of whitespace around the `<body>` element (and its children elements):

![img](/files/images/tutorials/devtools/body-style-element-padding.png)

Where did that style come from? If you look back in the __DOM Tree__, you'll see that the `<body>` element has an __attribute__ named `style`:

~~~html
<body style="padding: 50px;">
~~~

Throwing in style code into HTML `style` attributes is known as __inline CSS__, and it is __not recommended__. I use it here just to keep the examples simple, but remember that the point of CSS is to __separate presentation__ (e.g. `padding: 50px`) from __the content__ (e.g. the `<body>` element and its children)


### Linking to an external stylesheet:

The second listed style refers to the `body` element, and in the top-right corner of this section of code, there's a reference to `a-styles.css:1`. This tells us that the CSS in this snippet comes from an _external style sheet_:

![img](/files/images/tutorials/devtools/body-external-styles.png)


If you look through the DOM Tree and expand the `<head>` tag, you'll see an HTML element that instructs the browser to fetch a specific CSS file and apply its styles to the webpage:

~~~html
<link href="/files/pages/web-inspector/assets/a-styles.css" rel="stylesheet">
~~~

The URL in the `href` is __relative__ to the page's domain; its __absolute__ value is:

    http://www.compjour.org/files/pages/web-inspector/assets/a-styles.css

[Visiting that URL](/files/pages/web-inspector/assets/a-styles.css) will open up the CSS file. Remember that just because the browser can open and display a file from a URL (such as an image), it doesn't mean that what it displays is actually HTML; a CSS file is just plaintext:

![img](/files/images/tutorials/devtools/viewing-a-css-file.png)


## Interactively switching out the styles 

One of the best features of the brower's devtools is how it lets us tinker with the code of a webpage and see the result of the change _without having to reload the webpage_.

In the paragraph element (i.e. the `<p>` tag), do you wonder what the page would look like without that ugly green-colored text? Just click on the `<p>` element and then, in the Styles Pane, __deselect__ the `color` attribute, which has been set to `#383`:

![img](/files/images/tutorials/devtools/p-green-to-black.gif)


When we uncheck that `color` property, the browser looks for the next style code that refers to the color of text for paragraph elements. In this case, the next relevant style code (and it may be the default of the browser) is to render paragraph text as `black`.

Check out the other inline styles of [this wacky test page](/files/pages/web-inspector/inline/), which I've deliberately designed with _worst_ practices to illustrate the interaction between CSS and HTML. For example, look at the headline of `AMERICA!`. The browser renders it at the beginning of the page, so you might assume that the headline element is before both the image and the paragraph elements.

However, if you inspect the DOM tree, you'll see that the `<h1>` element is actually the _last_ element on the page. So why is it rendered at the beginning? Notice the inline style I've given it. Then, look in the Styles Paine and uncheck the corresponding properties to see where the `<h1>` element would be placed if browsers displayed HTML elements in sequential order:

![img](/files/images/tutorials/devtools/top-america-h1.gif)

To reiterate an earlier point: HTML is not what-you-see-is-what-you-get when it comes to the visual display of a webpage. CSS is where the visual properties of each element are defined.


## CSS selectors

For data programmers, the CSS syntax is not a huge priority to learn, unless you also want to build and design webpages. But let's assume you just want to collect data from webpages. Then, the relevant part of CSS is the concept of __[CSS selectors](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Getting_started/Selectors)__.

By understanding CSS selectors, we are able to write scraper code that can target specific groups of elements.


### Tag name

We already know the most basic kind of selector: HTML tags.

To make all hyperlinks be green in color and in bold font, we use `a` has a selector:

~~~css
a{
   color: green;
   font-weight: bold; 
}
~~~

What if we wanted to target only a subset of hyperlinks, such as ones that were within `<h2>` elements? To express a nested-relationship, we simply list the tag names in ascending order:

~~~css
h2 a{
   color: purple;
   font-weight: bold; 
}
~~~

The Python code to target all hyperlinks within `<h1>` headlines and print their `href` attributes looks like this:

~~~py
import bs4
import requests
soup = bs4.BeautifulSoup(requests.get('http://www.nytimes.com').text)
for link in soup.select("h2 a")['href']:
    print(link['href'])
~~~



### The `id` and `class` attributes

Besides tag names, the `id` and `class` HTML attributes are also used to narrow target elements. Perhaps there are multiple groups of `<h2>` elements and we want to affect only a single _class_:

~~~html
<h2 class="hit-me"><a href="/">Yes</a></h2>
<h2 class="not-me"><a href="/">No</a></h2>
~~~

The `class` attribute is specified in the selector syntax by using a __period__ before the class name:

~~~css
h2.hit-me a{
   color: purple;
   font-weight: bold; 
}
~~~

The `id` attribute works the same way, except a __pound__ sign is used in the selector syntax:

~~~html
<h2 id="hit-me"><a href="/">Yes</a></h2>
<h2 id="not-me"><a href="/">No</a></h2>
~~~

~~~css
h2#hit-me a{
   color: purple;
   font-weight: bold; 
}
~~~


### Scraping the headline selectors from nytimes.com

I didn't have the foresight to make a test page that clearly illustrated the use of `id` and `class` selectors, so I'll use a real-world example (as of April 2015, at least): the [New York Times homepage at www.nytimes.com](http://www.nytimes.com/)

This is what the HTML code on the NYT homepage looks like for the center headline:

![img](/files/images/tutorials/devtools/nyt-sample-h2.png)

Now, if I wanted to get _all_ of the main headlines, this CSS selector might work just fine:

        h2.story-heading

~~~py
import bs4
import requests
soup = bs4.BeautifulSoup(requests.get('http://www.nytimes.com').text)
links = soup.select("h2.story-heading")
# print out the number of links
print(len(links))
# 108
~~~


_However_, what if I want just the headline to the current front-center story? Check out the code listed in the Styles Pane to see a more specific selector:

        .photo-spot-region .story.theme-summary.lede .story-heading


Let's just use part of that:

~~~py
links = soup.select(".photo-spot-region .story.theme-summary.lede .story-heading")
# print out the number of links
print(len(links))
# 1
~~~

This tutorial is only meant to cover basics about CSS and not go into web-scraping, but hopefully you can see the relation the two concepts have. Learning CSS selectors, and the DOM tree concept overall, will make you a better scraper.



For more information, check out the Chrome DevTools tutorial on [Editing Styles And The DOM Introduction](https://developer.chrome.com/devtools/docs/dom-and-styles)
