---
title: Installing Python 3.4
curriculum_order: 35

---

Note: There are many ways to get a stable install of Python onto your system &ndash; I personally [go with __pyenv__](https://github.com/yyuu/pyenv) &ndash; but the [Anaconda package from Continuum Analytics](https://store.continuum.io/cshop/anaconda/) seems to ably fill all of our needs while being as simplified of a cross-platform installation process as possible.

Currently, the instructions below walk through the installation process for __OS X 10.7+__, but the steps in Windows should largely be the same. I'll update this page with more instructions if it turns out alternatives to Anaconda are needed.


The Anaconda installation package is __300MB__ by itself. When installed, Anaconda's Python will take up __1.9GB__.



## Installing Python 3.4 with the Anaconda installer

Setting up a programming environment can often be a show-stopping obstacle. Luckily for us, Continuum Analytics has created a [free, download-and-click installer for Python 3.4](http://continuum.io/downloads#py34) and a bundle of its most useful libraries.

The following steps are for Max OS X 10.7+, though they should be similar for Windows system. The important part is to make sure you're downloading the __3.4__ installer (and _not_ the 2.7 version of Python).


### Download the Anaconda 3.4 installer

[Download Anaconda 3.4](http://continuum.io/downloads#py34). This is what the installation page looks like:

![image](/files/images/tutorials/python/download-anaconda-button.png)


The installer package is more than __300MB__. After downloading the file, your __Downloads__ folder should have something like:

      Anaconda3-2.2.0-MacOSX-x86_64.pkg

![img](/files/images/tutorials/python/downloaded-anaconda-mac.png)


__Double-click__ the package file to launch the installer.

![img](/files/images/tutorials/python/welcome-to-anaconda-installer.png)

If possible, choose the __Install for me only__:

![img](/files/images/tutorials/python/install-anaconda-diskspace.png)


### Verify the Anaconda installation

If the installation goes smoothly, go to your __command-line__ prompt and type in the following commands:

~~~sh
which python
# /Users/dtown/anaconda/bin/python
python --version
# Python 3.4.3 :: Anaconda 2.2.0 (x86_64)

~~~

The respective responses should look similar, but not  _exactly_ the same. The most important part is the `Python 3.4.3 :: Anaconda 2.2.0` bit.

When I run those commands in my own Terminal, this is what I get:

![img](/files/images/tutorials/python/testing-anaconda-install-cli.png)




## Test out the libraries

With Anaconda successfully installed, you should now have access to the libraries and functions needed to carry out the vast majority of data/statistics/web-related programming tasks for this class.

Try out this simple scraping example, which fetches the page at [www.example.com], extracts the hyperlink, and prints out its `href` attribute (i.e the URL of the hyperlink):

~~~py
import requests
import bs4
response = requests.get('http://www.example.com')
soup = bs4.BeautifulSoup(response.text)
print(soup.find('a')['href'])
~~~

To __run__ this code, you can do one of two things: Create a Python script and run it from the command-line. Or, execute the code, line-by-line, in [__iPython__](http://ipython.org/).

### Create a Python script and run it from the command-line

1. Create a new text file named `example.py`
2. Write the commands given above into `example.py`
3. Save the file
4. From the command-line prompt, run this command:

        python example.py

You should see this result:

        http://www.iana.org/domains/example

Here's an animated GIF of the process:

![img](/files/images/tutorials/python/example.py.cli.gif)


### Execute code in iPython

[__iPython__](http://ipython.org/) is a command-line interface that lets you interactively execute code line-by-line. The end result is the same as writing a script and running it through the `python` interpreter, as demonstrated above. The difference is that with iPython, you can walk through the code as you execute it line-by-line.

This of course is slower than just putting code in a script file and executing it. But when you don't know yet what the code should be, __iPython__ is a great environment for tinkering with code and seeing how each command works.

Here's an animated GIF of the process. Note that at __line 4__, I hit the __Tab__ key to do an autocomplete, hence, the weird break in the code:


![img](/files/images/tutorials/python/example.py.ipython.gif)


Speaking of the __Tab__ key: taking the 5 to 10 minutes to build the muscle memory needed to reflexively hit [__Tab__ to autocomplete commands in iPython](http://ipython.org/ipython-doc/stable/interactive/tutorial.html#tab-completion) is one of __the easiest things you can do__ to increase your short- and long-term success rate at programming.

Check out the [official iPython tutorial](http://ipython.org/ipython-doc/stable/interactive/tutorial) for more tips and background on how to effectively work with Python.
