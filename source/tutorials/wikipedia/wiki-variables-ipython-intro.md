---
title: Introduction to iPython and Variables
group_title: Exploring Wikipedia
---


* TOC
{:toc .tock}

Open iPython:


[#snippet-1](#snippet-1){:#snippet-1}

~~~py
import requests
url = "http://stash.compjour.org/data/wikipedia/hi.html"
response = requests.get(url)
pagetext = response.text
print(pagetext)
~~~

The output of that __print()__ function will look like:

~~~
<html>
   <head><title>A hello page</title></head>
<body>
  <h1>Hello!</h1>
~~~



TKGIF

## Variable assignment

There's a lot going here. For now, just focus on line 2:

~~~py
url = "http://stash.compjour.org/data/wikipedia/hi.html"
~~~

This is an example of __variable assignment__. The term on the left side, `url`, is the __variable__. The term on the __right__ side is the _value_ that we're assigning to the variable named `url`.

Try this:

~~~py
print(url)
~~~

You should see the value of `url`

### Reassigning the value

~~~py
url = "whatever"
print(url)
~~~

TKGIF


### Variable "math"


[#snippet-2](#snippet-2){:#snippet-2}

~~~py
a = 'http://stash.compjour.org/data/wikipedia/'
b = 'hi.html'
c = a + b
print(c)
# http://stash.compjour.org/data/wikipedia/hi.html
~~~

### Why the quotes

One thing that should catch your eye:

~~~py
url = "http://stash.compjour.org/data/wikipedia/hi.html"
~~~

Why do there need to be quotes? Take a look at the other operations we've done:

~~~py
x = "a"
y = "b"
z = x + y
print(z)
# ab
~~~

Now try that _without_ the quotes around `a` and `b`:

~~~py
x = a
y = b
z = x + y
~~~

If you haven't messed around with `a` and `b` from our [earlier snippet](#snippet-2), the result should be the URL that is stored in the variable `c`. Why is that? 

`x = a` means "assign the value referred by _variable_ `a` to variable `x`"

`x = "a"` means "assign the value of the _letter_ `"a"` to variable `x`"

~~~py
a = "something"
x = a
print(x)
# someting
x = "a"
print(x)
# a
~~~

The main takeaway is, don't assume that the Python interpreter has the sentience of a third-grader: it will interpret you as _literally_ as possible. We'll save the concept of __data types__ &ndash; including what a fuller explanation of quoted __text strings__  &ndash; for a later lesson. It's enough to point out that __punctuation is important__.




## Back to the context of Wikipedia

Let's restart iPython. Type `exit` and hit Enter &ndash; this will kick you back to the command prompt. Type `ipython` and hit Enter to get back into iPython. All the variables &ndash; `a`, `b`, `url` &ndash; and what they pointed to are completely wiped away in this new session.

Let's use a Wikipedia-specific example:

[#snippet-3](#snippet-3){:#snippet-3}

~~~py
import requests
baseurl = 'http://en.wikipedia.org/wiki/'
a_title = 'Kansas'
url = baseurl + a_title
resp = requests.get(url)
print(resp.text)
# The result will be the raw HTML of the webpage found at
# http://en.wikipedia.org/wiki/Kansas
~~~

It looks different from [#snippet-1](#snippet-1), but it's essentially the same process, with differently named variables. Instead of `response`, I use `resp`. And instead of assigning the value of `response.text` (or `resp.text`) to a variable named `pagetext`, I skip using a new variable all together and just print the result of `resp.text`.

Let's reduce this a couple of steps:

~~~py
import requests
baseurl = 'http://en.wikipedia.org/wiki/'
a_title = 'Kansas'
print(requests.get(baseurl + a_title).text)
~~~

And now let's go all the way and reduce the snippet to its fewest-line form:

~~~py
import requests
print(requests.get('http://en.wikipedia.org/wiki/' + 'Kansas').text)
~~~

So you should ask: _Why even bother using variables when we can just get everything done the same in one line?_ There is no _one_ way to write a program, and that's a key lesson going forward. If your only goal was to dump the text of the Wikipedia entry for Kansas onto your screen, then the two-line snippet is just fine, though it's worth pointing out that we've sacrificed readability for line count, and that is a non-trivial tradeoff.

However, if your goal is to do something more _expansive_ than fetching and printing a single specific page, consider this variable-free code:

~~~py
import requests
print(requests.get('http://en.wikipedia.org/wiki/' + 'Kansas').text)
print(requests.get('http://en.wikipedia.org/wiki/' + 'Iowa').text)
print(requests.get('http://en.wikipedia.org/wiki/' + 'Hawaii').text)
~~~

And consider the _value_ &ndash; to the human reader/writer of the code, not the computer (which doesn't care either way) &ndash; of storing the repetitive part (think of it as the _constant_) in a variable:

~~~py
import requests
baseurl = 'http://en.wikipedia.org/wiki/' 
print(requests.get(baseurl + 'Kansas').text)
print(requests.get(baseurl + 'Iowa').text)
print(requests.get(baseurl + 'Hawaii').text)
~~~

One practical advantage that is of immediate relevance to us: if we want to change the first part of that URL, it's a lot easier to reassign `baseurl` than it is to replace it across three different lines:

~~~py
import requests
basepath = 'http://en.wikipedia.org/w/api.php?'
baseparams = 'action=query&prop=info&format=json&titles=' 
baseurl = basepath + baseparams
print(requests.get(baseurl + 'Kansas').text)
print(requests.get(baseurl + 'Iowa').text)
print(requests.get(baseurl + 'Hawaii').text)
~~~

And consider that in most worthwhile programming, you will not be iterating across 3 different values, but several hundreds, if not thousands and millions of values. With that in mind, the convenience of setting up a few variables quickly adds up.


## What we don't know

What about the rest of this webpage-downloading code? What is `import requests`, for example? What does `.text` mean? We'll cover those in subsequent lessons. The most important takeaway is that whether you're a beginner, or a master, attempting to read or write a non-trivial program, you will __always not know everything__ about its code. Much of the power and appeal of programming comes from being able to include and invoke someone else's packaged code with a single word (if you're curious, you can view the [documentation for the __requests__ library here](http://docs.python-requests.org/en/latest/)).

This easy reusability of code isn't just a "feature" of programming, it is an absolute necessity for all modern programmers, such that entire libraries and systems (you'll hear of __[pip](https://pip.pypa.io/en/stable/)__ soon) are built solely to streamline that process of reusability. 

So get used to encountering programming scripts and not knowing what 90% of it actually means (as you've seen, variables can be named just about whatever the author feels like). The path to understanding it is to immediately recognize the patterns you _do_ know. 

And for now, focus on being able to _visually_ recognize the pattern, and then understand the meaning of (and the difference between) these two lines:

        a = "b"
        b = a

And you should be able to derive the _result_ of these two subsequent lines:

        print(a)
        print(b)






