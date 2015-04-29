---
title: Introduction to Objects and Functions and a Few Keywords 
description: Python is made up of barely more than 30 keywords. The rest are shortcut-words to let us use other programmers' useful code.
---

You don't have to know very much about the Python language internals or even its vocabulary to do highly-productive tasks with it. Believe it or not, in this snippet of code:

~~~py
import requests
url = "http://stash.compjour.org/pages/hi.html"
response = requests.get(url)
pagetext = response.text
print(pagetext)
~~~

There is exactly __one__ special-to-Python keyword that you have to actually know. And what's the rest? It's either user-provided values (such as that URL), or words that refer to the pre-packaged code made by programmers that can be directly imported and used in our code. The trick in reading any given script is knowing which words (and patterns and structures) that you _just_ have to know. And which come from a third-party, in which case, you just have to read their docs (here's [the docs for __requests__ refers](http://docs.python-requests.org/en/latest/), for instance).




* TOC
{:toc .tock}

## Python's keywords

If you are overwhelmed by the variety and number of new terms thrown at you in a Python script, take comfort in knowing that there are actually very few [keywords that make up the Python language](http://en.wikipedia.org/wiki/Python_syntax_and_semantics#Keywords) &ndash. For Python 3.x, there are __32__ keywords for Python 3.x, and roughly half of those (in __bold__ below) we'll encounter on a regular basis:


| __and__   | del       | __from__   | nonlocal   | try      |
| __as__    | __elif__  | global     | __not__    | while    |
| assert    | __else__  | __if__     | __or__     | __with__ |
| break     | except    | __import__ | pass       | yield    |
| __class__ | __False__ | __in__     | raise      |          |
| continue  | finally   | __is__     | __return__ |          |
| __def__   | __for__   | lambda     | __True__   |          |
{:.table}

And in these lessons, I skip such concepts as [object-oriented programming](https://docs.python.org/3/tutorial/classes.html), so maybe just __12__ of these keywords are fundamentally important to memorize (with the others being variants/extensions of those, such as `while` to `for`, and `elif` to `if` and `else`):

|and|False|import|not|True|
|def|for|is|or|
|else|if|None|return|
{:.table}


So this means that for the script at the beginning of this lesson, there is exactly __one__ Python-language keyword in that entire script, which I've bolded below:

<pre>
<strong>import</strong> requests
url = "http://stash.compjour.org/pages/hi.html"
response = requests.get(url)
pagetext = response.text
print(pagetext)
</pre>

So besides the variable names that are made up by us (`url`, `response`, `pagetext`), what are all the other words (`requests`, `get`, `print`)? They refer to either __functions__, __methods__, __attributes__, or __modules__.


## Functions

When a non-keyword (i.e. _not_ something such as `if`) is _immediately_ followed by an __opening parentheses__, i.e. `(`, you should interpret that as a __function__ being _executed_.

In the following line is the most minimal execution of the `print()` function, which prints a blank line to the screen:

~~~py
print()
# [a blank line]
~~~

Normally, we want to print _something_ with `print`, e.g:

~~~py
print("hello")
# hello
~~~

The text value of `"hello"` is the __argument__, i.e. an object for `print()` to _act_ upon, in this case, printing it to the screen.

The `print()` function can take multiple arguments. In that situation, it just prints each argument consecutively, separated by a space:

~~~py
print("hello", "mom", "!!!")
# hello mom !!!
~~~

Why does `print()` print those arguments with a space-in-between, rather than unseparated? Because that's how `print()` was defined by its author. If we want something different, we have to define our _own_ function.

We'll cover the purpose and syntax of defining functions in more detail later; for now, it's just enough to know that it can be done:


~~~py
def smushprint(a, b, c):
    d = a + b + c
    print(d)

smushprint("hi", "dad", "!!!")
# hidad!!!
~~~

(note: this simple proof-of-concept function is _seriously_ flawed; try running it with just _one_ argument)


### Functions as labels

If we think of __variables__ as a sort-of _label_ for data values, then think of functions as another kind of _label_, but for code that is meant to be __called__, (which I also referred to as _executed_). Just as it's convenient to give a human-readable/writeable name to a complicated text string for later reference, it's convenient to give a label/nickname to a series of expressions that we intend to execute again.

One consequence of functions being a type of _label_ is that this is something that works (even if it seems nonsensical):

~~~py
booya = print
booya('kasha')
# kasha
~~~


## Modules

The `import` keyword allows your current script (or iPython session) to bring in prepackaged code.

Thus, the following line:

~~~py
import requests
~~~

&ndash; allows subsequent code to have access to the module named [__requests__](http://docs.python-requests.org/en/latest/), e.g:

~~~py
requests.get("http://www.example.com") 
~~~

How is `requests` different from the function named `print`? Well, for starters, we don't __execute__ the `requests` module. The following code will cause an error:

~~~py
requests("http://www.example.com")
# TypeError: 'module' object is not callable
~~~

However, just as `print` is a label/reference to some kind of executable routine, think of the name `requests` as being a sort of label for a package of code. And so, this is a valid expression:

~~~py
import requests
demands = requests
demands.get("http://example.com")
~~~

Just a sidenote: if you really want to rename something you've imported (which is uncommon), the standard practice is to use the `as` keyword:

~~~py
import requests as demands
~~~


## The type() "function"

By this point, you should be seriously wondering, _"How the hell do you keep track of what's a function, a module, a variable, or whatever?"_. The pragmatic answer is: _don't import or introduce a bunch of things you have no clue about_. In the case of the [requests library](http://docs.python-requests.org/en/latest/), I know that it is a well-loved solution to the tedious process of setting up HTTP connections, so I take the time to read its very thorough documentation and examples.

That said, there is frequent occasion to check on an object's _type_. And for that, there is the [built-in function named __type__](https://docs.python.org/3/library/functions.html#type).

The simplest call of the `type()` function is to pass in an object. The resulting value will be the __type__ of that object:

~~~py
type(42)
# int
type(42.0)
# float
type("42")
# str
type(str)
# type
type(print)
# builtin_function_or_method
~~~




Note: if you try `type(type)`, the return value will be `type`, even though I've described `type()` as a function. The exact mechanics here are more nuanced and not worth getting into detail about, especially as I'm sidestepping the depths of object-oriented programming and [Python's __class__ mechanism](https://docs.python.org/3/tutorial/classes.html).


## Objects and Types

So one takeaway of trying out the `type()` function is that `42` is a `"42"` are two different _types_ of __objects__, `int` (short for __integer__) and `str` (short for __string__), respectively. In fact, in Python (and in other similarly high-level languages), __everything is an object__.

But what does that mean exactly? In programming, an __object__ is said to have __methods__ and __attributes__. OK, what does _that_ mean? In the real-world, if you think of a bicycle as being a kind of _object_, you might say that for any given _instance_ of a bicycle (such as, "Dan's bicycle"), you can think of it as having __attributes__ of `color` and `weight`, and __methods__ of `brake()` and `ring_the_bell()`.


Back to the programming world. Each __object__ has a set of __attributes__ and __methods__ that belong to it. To refer to these, we append a __dot character__ to an object, then type in the name of the attribute or function.

In the snippet below, I invoke the `upper()` __method__ (think of methods as similar to functions), which belongs to the object (`"hey you"`) represented by the variable `x`:

~~~py
x = "hey you"
x.upper()
# "HEY YOU"
~~~

### Attributes


Let's take the object `"42"`, which is an _instance_ of  the `str` (a text string) __type__. The object `"42"`, like all other strings, has an __attribute__ named `doc`, which contains some documentation for `str`:

~~~py
n = "42"
print(n.__doc__)
# str(object='') -> str
# str(bytes_or_buffer[, encoding[, errors]]) -> str
#
# Create a new string object from the given object. If encoding or
# errors is specified...
~~~


### Methods

Think of a __method__ as a __function__ that belongs to an object. So, using the object `"42"` again, we can see that it has several methods that can act on it:

~~~py
n = "42"
n.isnumeric()
# True
n.isalpha()
# False
n.replace('4', 'forty')
# forty2
~~~

### Tab for autocomplete

This is a tip I should've mentioned at the very beginning of this lesson; even though it is a keyboard-shortcut, it is _essential_ in learning Python and writing complicated programs.

At the iPython prompt, type in:

~~~py
xxkjsdhfkjsadhf = "hello"
~~~

Pretend that somewhere later in your session, you actually need to refer to that variable. And the only thing you remember about it is that it begins with `xx`. 

So type in `xx`, and __then hit the Tab key__

iPython should __autocomplete__ the rest of the variable name for you.

Now, with `xxkjsdhfkjsadhf` spelled-out at the prompt, type a __dot character__, and then hit the __Tab__ key. What you should then see is a list of all available methods for the `xxkjsdhfkjsadhf` object (which is the text string `"hello"`).

If you then type `f`, and hit __Tab__ again, the list of methods will be filtered to those that start with `f`.

In GIF form:

GIFTK


The list of methods that belong to text string; you, nor any human, can't possibly be expected to remember what they all are. That's the computer's job. So make use of that fact by hitting the __Tab__ key as an _instinctive_ action.


### Different types don't (usually) mix

If you test out the attributes and methods for the integer object of `42`, you'll see that it has different methods and attributes. For example, it doesn't have `isnumeric()` (which returns `True` or `False` if a text string contains all numbers) because, by definition, an integer _is_ "numeric".

So if `"42"` and `42` are two different _types_ of objects, what is the result of this expression:

        "42" + 42

Is it `84`, `4242`, or `"4242"`? If you run that expression in iPython, you'll get an error which can basically be interpreted as: _you are trying to add two different things which makes no sense or has any "correct" answer. Stop and think about it_.

No need to go into much more detail about this except to note that many, _many_ of your errors will be "type errors".


## USAJobs code

Let's use a more real-world example involving the __requests__ library and the USAJobs API. Refresh your memory of what the following URL looks like in your web browser:


[https://data.usajobs.gov/api/jobs?Country=Iraq](https://data.usajobs.gov/api/jobs?Country=Iraq){:.rawurl}

Now access it via iPython:

~~~py
import requests
url = "https://data.usajobs.gov/api/jobs?Country=Iraq"
resp = requests.get(url)
txt = resp.text
print(txt)
~~~

Things that should be evident or derivable by you:


- `requests.get()` is a __method__ belonging to the `requests` __module__
- `text` is an _attribute_ of `resp.text`
- The value of `resp.text` itself (which, above, has been assigned to the `txt` verible), is an object of __type__ `str` (do `type(txt)` to check yourself).

One thing that you should wonder about? What _exactly_ is that `resp` object?

It turns out to be a `Response` object (which is part of the `requests` module). Why doesn't `resp` just contain the raw text what exists at the URL? Because the designer of the __requests__ package thought that it'd be more useful to create an object that held all the various components of a response from the web server, including the metadata that's passed as part of every web request:

~~~py
type(resp)
# requests.models.Response
resp.status_code
# 200
resp.is_permanent_redirect
# False
resp.ok    
# True
~~~

One method we'll find especially useful is the `Response` object's method, `json()`:

~~~py
data = resp.json()
type(data)
# dict
print(data['TotalJobs'])
# 6
print(data['Pages'])
# 1
~~~

What is a `dict` object? It's short for "dictionary", and we'll cover that data structure in the next lesson. (note: this lesson is not done...so check out other documentation on lists and functions):

- [https://docs.python.org/3.4/tutorial/datastructures.html](https://docs.python.org/3.4/tutorial/datastructures.html)
- [Dictionaries via LPTHW](http://learnpythonthehardway.org/book/ex39.html)
