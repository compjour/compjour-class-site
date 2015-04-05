---
title: Elements of a Webpage
description: Using Chrome DevTools to inspect HTML structure
curriculum_order: 21

nav:
  part_of: intro-to-the-web-inspector
  next: styles-of-a-webpage
---


## Everything is just text

(rambling about HTML, the nature of data, web, etc. TK)

## A brief primer to HTML

It's worth knowing a minimum of HTML terminology before we begin debugging web pages. 


Here is the raw HTML code behind a single __HTML element__:

~~~html
<strong>Hello</strong>
~~~

An HTML element contains a __tag__, or more often, a __starting__ and __closing__ tag. In this case, the __tag__'s name is `<strong>`, and the element consists of both a __starting tag__ &ndash; `<strong>` &ndash; and a __closing tag__ &ndash; `</strong>`.

The word `Hello` is a raw text element. As it's contained within the starting and closing `<strong>` tags, we can think of the `Hello` text element as being a __child__ of the element denoted by the `<strong>` tag.

When the above snippet is _rendered_ by the browser, this is what the element looks like:

---

<strong>Hello</strong>

---

### Attributes

Not all HTML elements contain a pair of tags, nor have children elements. For instance, here's the `<img>` tag used to denote an image element:

~~~html
<img src="http://www.compjour.org/files/images/stanford-pano.jpg" alt="Stanford">
~~~


While the `<img>` tag is lone and childless, it does contains two __attributes__: 

- `src` - the URL for the actual image file
- `alt` - the text to show if the image file URL is invalid, or if the page is being read by a non-visual browser (such as a screen-reader for the visually impaired).

__Note:__ For HTML elements that consist of a starting and closing tag, the attributes are always defined in the __starting tag__.


As I stated earlier in this lesson, HTML documents are __just text__. When the browser renders multimedia elements, such as photos and movies, it's a result of the browser following the URLs denoted in the HTML elements' attributes.

In this case, the `<img>` element has a `src` attribute which points to where the browser can find a photo to display:

---

<img src="http://www.compjour.org/files/images/stanford-pano.jpg" alt="Stanford">

---

We can visit the URL directly by copying and pasting the URL below into the browser's address bar:

      http://www.compjour.org/files/images/stanford-pano.jpg

Be careful not to mistake the result of this copy-pasting-hitting-Enter as visiting an actual webpage. Instead, what a modern web browser will do is just act like an image viewer. Since we're still in the web browser, it _seems_ as if it's an actual webpage:

![not an actual webpage](/files/images/tutorials/devtools/not-a-webpage.jpg)




### Nested elements

The raw HTML for a __hyperlink__ looks like this:

~~~html
<a href="http://www.stanford.edu">Stanford's homepage</a>
~~~

(Why `<a>`? Hyperlinks are also referred to as __anchor tags__)

Again, `href` is the __attribute__, and `http://www.stanford.edu` is the value of that attribute. The `<a>` tags contain the raw text element `Stanford's homepage`. This is how the browser renders that snippet:

---

<a href="http://www.stanford.edu">Stanford's homepage</a>

---

However, HTML tags can contain other tags as well. In the following snippet, a hyperlink contains an image element &ndash; i.e. the image is the _child_, or is _nested_, within the hyperlink:

~~~html
<a href="http://www.stanford.edu">
<img src="http://www.compjour.org/files/images/stanford-pano.jpg" alt="Stanford">
</a>
~~~

The browser renders this code as an image that, when clicked, will send the user to `http://www.stanford.edu`:

--- 

<a href="http://www.stanford.edu">
<img src="http://www.compjour.org/files/images/stanford-pano.jpg" alt="Stanford">
</a>

---





### The DOM Tree

__DOM__ is short for __Document Object Model__, and __DOM tree__ is [the term used](http://en.wikipedia.org/wiki/Document_Object_Model) to refer to the internal representation of a given webpage, i.e. the HTML elements as interpreted by the browser.

It's easiest to liken the "tree" of a HTML document to a _family tree_, in which each node/person has a __parent__. And some nodes also have __children__ elements, which are often referred to as __nested__ elements.

In the example snippet below, you can think of `<html>` as being the __root__ of the tree. The `<head>` and `<body>` are its __children__ elements, and they each have a child element of their own, `<title>` and `<h1>`, respectively:

~~~html
<html lang="en">
  <head>
    <title>Hello</title>
  </head>
  <body>
    <h1>Some words</h1>  
  </body>
</html>
~~~


And that's pretty much all we need to know about HTML. Yes, there are many, _many_ more varieties of tags and attributes. But we know enough to kind of understand the core concept of HTML: it's a particular format of text used to describe the structure of a webpage. Everything else will just be details to memorize on a need-to-remember basis.

If you want to learn a little more, here are some resources:

- [HTML Dog](http://www.htmldog.com/)
- [Codecademy's interactive HTML tutorial](http://www.codecademy.com/courses/web-beginner-en-HZA3b/0/1?curriculum_id=50579fb998b470000202dc8b)


## The Elements Panel

The Chrome DevTools __Elements Panel__  lets us interactively explore the DOM tree of the webpage currently rendered in the browser.

On the DevTools menu bar, __Elements__ is the first labeled item from the left. The panel contains two panes: On the _left_ is the __DOM Tree Pane__. On  the _right_ is the __Styles Pane__, which I'll cover in the next lesson. For the current lesson on the DOM tree, you can shrink the Styles Pane by dragging the divider-line:

![img](/files/images/tutorials/devtools/resize-elements-panel.gif)



### Using the "Inspect Element" pop-up menu command

Besides using the keyboard shortcut (__PC:__ <kbd class="kbd">Ctrl</kbd>+<kbd class="kbd">Shift</kbd>+<kbd class="kbd">I</kbd> / __Mac:__ <kbd class="kbd">Cmd</kbd>+<kbd class="kbd">Opt</kbd>+<kbd class="kbd">I</kbd>) to open the Dev Tools, the mouse can be used to jump right into the Elements panel:

1. __Right-click__ the element you want to inspect. This will bring up a pop-up menu.
2. Select __Inspect Element__

![img](/files/images/tutorials/devtools/inspecting-elements-right-click.gif)


This will conveniently bring up the __Elements__ panel and highlight the exact element we're interested in:

![img](/files/images/tutorials/devtools/inspect-h1-example.png)



## Interacting with the elements

The Elements panel makes it easy to see which bit of HTML code applies to which rendered page element. As we hover the mouse pointer over HTML code in the Elements panel, the corresponding rendered element will be highlighted. In the panel, an HTML element that contains __children__ nodes can be expanded to show its contents by clicking the adjacent little black arrow:

![img](/files/images/tutorials/devtools/inspecting-elements-perusing-the-dom.gif)



The Elements panel also makes clear the nested structure of HTML documents: hovering over the main `<body>` element highlights all of the visual content on the page. As you hover to each child element, from the `<div>` to the `<h1>` (i.e. the main headline, `Example Domain`), the visual highlight gets narrower and narrower:

![img](/files/images/tutorials/devtools/inspecting-elements-nested.gif)

Understanding the nested structure of HTML documents will be key to effectively doing web scraping. For example, we'll often want to target elements within a given parent element, rather than all elements across the document. 


### The breadcrumbs bar

The [webpage](http://www.example.com) we've been exploring in this example is extremely simple. In practice, webpages will contain a mess of HTML code that makes it difficult to track which child elements belong to which parents.

As you hover around the elements in the DOM Tree Pane, take a look at the very bottom of the Chrome browser: there's a __breadcrumbs bar__ that gives a one-line representation of what element we're pointing to, and all of its ancestors:

![img](/files/images/tutorials/devtools/inspecting-elements-tree-bar.gif)

As we go deeper and deeper into the DOM tree, the breadcrumbs trail gets longer and longer:

![img](/files/images/tutorials/devtools/inspecting-elements-tree-bar-closeup.gif)

### An example web-scrape

When we write web-scraping scripts, the breadcrumbs bar makes it very easy to find a reference the exact element we want to scrape. For example, we see that the hyperlink on `www.example.com/` exists at `html body div p a`.

To select this element in __Python__ (using the [Beautiful Soup HTML parsing library](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)) and print the URL it points to:

~~~py
import bs4
import requests
soup = bs4.Beautifrequests.get('http://www.example.com').text
print(soup.select("html body div p a")[0]['href'])

# http://www.iana.org/domains/example
~~~




## What we see is not what we get

Why do we care about exploring the internals of a webpage when we have a sophisticated web browser to render the page in a friendly, usable interface? Because not every detail about a page is revealed in that interface (that's why it's actually _usable_). And sometimes we don't care about what the page looks like; we want the data and other files that that page refers to.

Exploring the Elements panel is an essential step in both understanding how the Web works and, more directly, accessing data without letting an interface get in our way.


