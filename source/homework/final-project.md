---
title: Final Project Guide and Information
points: 50
due: 2015-06-09
description: |
  A public, deployed data project that provides an interesting view into public data.
---

* The TOC
{:toc .tock}

### Deliverables

__Due date:__ <%= homework_due_date %>


~~~
compjour-hw/
  |_____ final-project/
      |______ update.md
      |______ memo.md
      |______ and anything else
~~~


### Overall mindset

- Realize that we live in an abundance of information but with a scarcity of attention. It's not that information doesn't exist, but that we have trouble getting people to pay attention. __Think about what you can do to filter the noise__
- As humans, we are terrible at remembering not just what happened in the past, but at what _rate_ and _frequency_. The most [useful view on this Chicago Tribune crime app](http://crime.chicagotribune.com/chicago/community/east-garfield-park) is the month-over-month change in crime; at a glance you can tell if things are getting better or worse, and for how long.
- And the picture doesn't need to be _big_; focus on the details if there's a story here. This is a [single article about a single death in New York](http://iquantny.tumblr.com/post/95097770919/fatal-cyclist-accident-this-morning-was-tragically); what's compelling is the use of obvious, but easily forgettable statistics on past deaths. Think of how much work it was for one person, a professional analyst, to dig that up. For 99% of other people, the thought doesn't occur to look for past records. You sometimes don't have to be clever, just curious.

### Guidelines

From [the memo assignment page](/homework/final-project-memo):


#### It must be public-facing

(i.e. on the web and linkable, not in some zip folder you email me)

#### Deals with a public issue

#### Uses public data

#### You can work with a partner


### Design requirements

I know most of you aren't front-end designers. Still, try to make things look neat. In fact, if you throw on the [Bootstrap framework on your HTML page](http://getbootstrap.com/), you'll be mostly there. But mostly, I want a clean conceptual design. It should not be harder to find information on your project than it is on whatever you were hoping to supplant.


### Good readings

- [Source OpenNews guides to News Apps](https://source.opennews.org/en-US/guides/)
- [ProPublica Nerds Blog](http://propublica.org/nerds)
- [NPR Visuals Blog](http://blog.apps.npr.org/)
- [NICAR conference links via Chrys Wu](http://blog.chryswu.com/tag/nicar/)


## Tools

### Deployment

Note: deployment is hard. Make sure your thing works on your own computer first. Then, feel free to talk to me.

#### Frozen Flask and Github Pages

So getting your site online, in whatever form it is, is a bit tricky...again, I point you to Ben Welsh's excellent [First News App guide](http://first-news-app.readthedocs.org/en/latest/)...the [last section demonstrates one way of getting the app onto Github Pages](http://first-news-app.readthedocs.org/en/latest/#act-5-hello-internet) using a library called ["Frozen Flask"](http://pythonhosted.org/Frozen-Flask/)


#### Github pages

It's possible to dump raw HTML files and have them hosted on [Github Pages](https://pages.github.com/). However, you cannot run Python script on their servers.


#### Heroku

Heroku provides a mostly-push-button service to deploy an app...but you have to be relatively comfortable with the command line. [Here's one official guide](https://devcenter.heroku.com/articles/getting-started-with-python-o). One benefit of Heroku is that it is free.

I've [put up a sample app that I was able to deploy on Heroku](https://github.com/dannguyen/flask-firerain)...Two main differences from the Heroku tutorial are:

- Making your own [requirements.txt](https://github.com/dannguyen/flask-firerain/blob/master/requirements.txt) (a list of third-party libraries that you import)
- [Creating a runtime.txt](https://github.com/dannguyen/flask-firerain/blob/master/runtime.txt) that specifies Python 3.4.3

#### Amazon EC2

[Amazon EC2 is another cloud service with a free tier](http://aws.amazon.com/free/). It's a bit more do-it-yourself than Heroku. Here's a [guide on Flask from them](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html).

-------------


## Front end HTML/CSS 


[Just use Bootstrap](http://getbootstrap.com/getting-started/)


Include this in your HTML head:

~~~html
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
~~~

### Javascript libraries and widgets


- [Leaflet has some easy mapping](http://leafletjs.com/examples.html)
- [CartoDB is cool, though requires use of their content-management system](https://cartodb.com/)
- You can upload your data as a [CSV to Fusion Tables](http://www.smalldatajournalism.com/projects/one-offs/mapping-with-fusion-tables/)
- The [Bootstrap library](http://getbootstrap.com/javascript/) has some JavaScript components, though I don't know if you'll need them.


### Quickest way to get a plain HTML webpage up and tested

##### 1. In Sublime Text, create a new HTML file somewhere.

##### 2. Add this barebones HTML

I've included the bootstrap.css tag:

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Whatever</title>
</head>
<body>
   <!-- wrapping things up in the "container" class keeps things neat -->
  <div class="container">
    <h1>Some title</h1>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptat </p>
  </div>  
</body>
</html>
~~~

[Bootstrap docs are here](http://getbootstrap.com/getting-started/
). Google around for other guides. It's hugely popular.


##### 3. Save the file, pop open the Terminal

And go to the directory in which the file exists.

Then run this command to start a quickie webserver (similar to `app.py` [for the Flask app, except you don't need a flask app set up](http://first-news-app.readthedocs.org/en/latest/)):

      python -m http.server

It should display this message:

~~~
Serving HTTP on 0.0.0.0 port 8000 ...
~~~

Which means you can visit the page at [http://localhost:8000](http://localhost:8000)
