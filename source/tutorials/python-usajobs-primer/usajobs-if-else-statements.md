


https://docs.python.org/3/tutorial/controlflow.html

With loops, we can write a program that runs on its own for as long as we tell it to go. But what happens when a _decision_ has to be made?


Let's grab the first __250__ jobs listed for __California__:

~~~py
import requests
baseurl = "https://data.usajobs.gov/api/jobs"
s = "California"
resp = requests.get(baseurl, params = {"CountrySubdivision": s, "NumberOfJobs": 250 })
data = resp.json()
jobs = data['JobData']
~~~

How many of these are __full-time__ jobs? Each job dict has a `"WorkSchedule"` attribute. And so we want to count how many in the `jobs` list have the value `"Full Time"` for the `"WorkSchedule"`.

Let's pretend we wanted to just count how many items were in the `jobs` list (i.e. manually implement `len(jobs)`):

~~~py
jobcount = 0
for j in jobs:
    jobcount += 1

print("There are", jobcount, 'jobs')
# There are 250 full-time jobs
~~~



## Basic if syntax

To count full-time jobs, for each iteration of the loop, we want to increment `jobcount` _only_ __if__  a job has `"WorkSchedule"` of `"Full Time"`. For that, we need an __if statement__. Here's a basic example of an `if`-statement, which I've wrapped up in a function; Like the `for`-loop, we create a "block" of code that "belongs" to the `if`-statement:

~~~py
def foo(x):
    print("Testing...")
    if x > 100:
        print("x is big")    
    print("Test is done")
~~~

Calling `foo()`:

~~~py
foo(999)
# Testing...
# x is big
# Test is done

foo(10)
# Testing...
# Test is done
~~~


In other words: 

> _if_ the condition `x > 100` is `True`, then print `"x is big"` 

Notice in the `foo(10)` call, that the rest of the function runs as if the if-statement's code block wasn't there.

Let's insert an __if__-statement to the job-counting code:

~~~py
jobcount = 0
for j in jobs:
    if j['WorkSchedule'] == 'Full Time':
        jobcount += 1

print("There are", jobcount, 'full-time jobs')
# There are 185 full-time jobs
~~~

This works because when `j['WorkSchedule']` is _not_ equal to `Full Time`, then `jobcount` doesn't get incremented, and the loop moves on to the next iteration.


## Basic else syntax

With just a single `if`-statement, the program either executes the conditional block of code (__if__ the condition is `true`), or it jumps to the next part of the code after the block, as if that block didn't exist.

However, what if we wanted our program to do something _else_ if the `if` condition evaluates to `False`? Then we include an `else` statement:

~~~py
def foo(x):
    print("Testing...")
    if x > 100:
        print("x is big")
    else:
        print("x is weak")    
    print("Test is done")
~~~

Calling `foo()`:

~~~py
foo(999)
# Testing...
# x is big
# Test is done

foo(10)
# Testing...
# x is weak
# Test is done
~~~


Let's add an `else` branch to our job-counting code:


~~~py
ft_jobcount = 0
nonft_jobcount = 0
for j in jobs:
    if j['WorkSchedule'] == 'Full Time':
        ft_jobcount += 1
    else:
        nonft_jobcount += 1 


print("There are", ft_jobcount, 'full-time jobs')
print("There are", nonft_jobcount, 'full-time jobs')
# There are 185 full-time jobs
# There are 65 full-time jobs
~~~


### The `elif` statement

What if we need more than two branches? Then we can supply as many `elif` statements (short for, "_else if_") as we need:

~~~py
def what_animal(animal):
    if animal == "Cat":
        print("Meow")
    elif animal == "Dog":
        print("Woof")
    elif animal == "Llama":
        print("Burp")
    else:
        print("Zzzz")
~~~

The program flow can get quite complicated here, and logic errors can be very subtle. So as you start out, it's best to reduce things to `if/else` whenever possible. 

Speaking of subtle logic errors, compare the function above to this one:

~~~py
def what_animal(animal):
    if animal == "Cat":
        print("Meow")
    if animal == "Dog":
        print("Woof")
    if animal == "Llama":
        print("Burp")
    print("Zzzz")
~~~

Think of all the ways this slightly-changed `what_animal()` function drastically differs from the intention and behavior of the original `what_animal()` function.



### Exercise 1: Be picky about possible jobs

Pretend you're looking for a 

