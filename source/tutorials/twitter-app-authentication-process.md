---
title: Twitter App Authentication Process
---

This is a quick walkthrough of how to create a Twitter app using your main Twitter account, and have it be used by your secondary accounts.


* TOC
{:toc .tock}





By __main Twitter account__, I mean, _the Twitter account that has been authenticated and tied to your phone number_ &ndash; because Twitter won't let you create apps from a Twitter account without phone verification.

By __secondary accounts__, I mean any other Twitter accounts you may have created that haven't been tied to a working phone number.


At the end of this, you should have a file __somewhere on your computer__ (preferably in your home directory, such as `~/Desktop/tw.json`, or `~/tw.json`), that looks like this:

~~~json
{
    "consumer_key": "JKSADFJKLfdJASKDF",
    "access_token_secret": "ASDIFJ3iusaodfj",
    "consumer_secret": "JASKDFLJASDLKFJ39uasdfmljdsafkl3",
    "access_token": "98asdfkl3j-ASJDFKASJDF"
}
~~~



### 1. Create a new app with your main account

From your __main twitter account__ , visit [https://apps.twitter.com/app/new](https://apps.twitter.com/app/new) to create a new application. If you've never done this before, Twitter will ask you to verify your main twitter account via SMS message:


![img](/files/images/apis/twitter-create-an-app-screen.png)


After the app is created, click the __"Key and Access Tokens"__ tab. And note the values of __Consumer Key (API Key)__ and __Consumer Secret (API Secret)__.

![img](/files/images/apis/twitter-key-and-access-tokens.png)


### 2. Login with a secondary account via a different browser

Now open an __entirely different browser__. So if you used Google Chrome to log in as your __main account__, open up Firefox (or Internet Explorer, or Safari, or, more conveniently, [create a new user profile for Chrome](https://support.google.com/chrome/answer/2364824?hl=en)). 

Then go to [Twitter homepage](https://twitter.com) and log in as your __secondary account__.


### 3. Authenticate the secondary account with your app

Go to your text editor and open up a blank file. Copy-and-paste the following code into that blank file:

~~~py
import tweepy
CONSUMER_KEY = "YOUR_CONSUMER_KEY"
CONSUMER_SECRET = "YOUR_CONSUMER_KEY_SECRET"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# the following command will print a URL to visit:
print(auth.get_authorization_url())
~~~

The browser for your __main__ account should still be open to the __"Key and Access Tokens"__ page for that app you recently created. Now is the time to copy-and-paste the values for __Consumer Key (API Key)__ and __Consumer Secret (API Secret)__ into the string values for the variables `CONSUMER_KEY` and `CONSUMER_SECRET` in the snippet above.

When that's done, __copy__ that code snippet.

Then open up a command-line prompt (e.g. Terminal).

Then type `ipython` and hit __Enter__.


#### From inside iPython 

Now you should be in the __iPython__ prompt. Assuming the code snippet is still copied to your clipboard, at the iPython prompt, type:

~~~py
%paste
~~~

And hit __Enter__ to execute it. This `%paste` is a special iPython-only command that will paste what was in your operating system's clipboard into the iPython prompt:

![img](/files/images/apis/twitter-auth-flow-ipython-paste.png)

The result of that code snippet will print a __URL__ to screen that looks something like: 

    https://api.twitter.com/oauth/authorize?oauth_token=something

__Copy__ that URL and paste it (this is important) into the browser for your __secondary user__. If you do it using your __primary__ user, the world won't be destroyed, but you'll be creating credentials for your primary account...and the purpose of this was to create credentials so that you could tweet from your __bot__ account.

Visiting that URL will bring you to a page asking you to confirm the authorization request:


![img](/files/images/apis/twitter-auth-authorize-an-app.png)


Clicking __Authorize app__ will get you a PIN number:


![img](/files/images/apis/twitter-auth-get-pin.png)


Copy that to your clipboard. OK, now switch back to your __command-prompt__ and paste the following line into iPython (before you paste, replace `"THAT_PIN_NUMBER"` with the actual PIN number you just received):

~~~py
token = auth.get_access_token(verifier = "THAT_PIN_NUMBER")
mycreds = {
  'consumer_key': CONSUMER_KEY,
  'consumer_secret': CONSUMER_SECRET,
  'access_token': token[0],
  'access_token_secret': token[1]
}
~~~


OK, if all went well, the `mycreds` variable should now point to a dictionary of the key-value pairs needed to programmatically login to Twitter.

## Test out Tweepy

Let's test it out; paste the following into iPython:

~~~py
t_auth = tweepy.OAuthHandler(
             consumer_key = mycreds['consumer_key'],
             consumer_secret = mycreds['consumer_secret']
)
t_auth.set_access_token(
      mycreds['access_token'],
      mycreds['access_token_secret']
)
the_api = tweepy.API(t_auth)
~~~

At this point, the `the_api` variable should point to an object that, well, is filled with methods that call the Twitter API, including `me()`, which simply fetches the data object for the currently authenticated user. 


So the result of the following snippet should print to screen the authenticated (i.e. your __secondary__) account's screen name:

~~~py
me_obj = the_api.me()
print("The currently authenticated screen_name is: ", me_obj.screen_name)
~~~

If the app you created had __read-and-write__ permissions, the following Tweepy command should send out a new Tweet from your secondary account:

~~~py
the_api.update_status(status = "Look at me using tweepy")
~~~

If you visit Twitter using the browser from which you logged in as your __secondary account__, you should see that new Tweet in your user timeline.


## Save and Repeat

Did that process seem incredibly cumbersome? Can you imagine going through it every time you wanted to send a Tweet programmatically? I hope not; even if you could redo it, typo-free, in two minutes or even 10 seconds, that makes it too slow for practical programmatic use. 

Luckily, we can re-use what's in the `mycreds` variable. But when we close the current iPython session (e.g. by typing in `exit`, or shutting off the computer), all the data held in the session's variables will just disappear.

So what we need to do is save the contents of the `mycreds` variable into a __text file__. Forgot what's in it? Run this at the iPython prompt:

~~~py
print(mycreds)
~~~

You should get something that looks like this:

~~~py
{'consumer_secret': 'blahblahconsumersecret', 'access_token': 'blahblahaccesstoken', 'consumer_key': 'blahblahconsumerkey', 'access_token_secret': 'blahblahaccestoken'}
~~~

### Saving the file to disk

What iPython prints to screen is pretty much actual JSON. In fact, you can save your authentication data in this crude fashion:

1. Copy the printed output of `mycreds` to your clipboard
2. Open up a new text file in your text editor. 
3. Paste the contents of the clipboard into the new text file.
4. Save the file.

Note: You may have to do a little find-and-replace so that Python can read that JSON file: find all __single-quotes__ and replace with __double-quotes__.


Now, this "Save the file" step is technically like saving any other file you've ever saved before. But you need to be extra, __extra__ aware of where you save this file. For starters, any programming script that wants to use those credentials will have to, well, open that file at whatever location you saved it to.


My recommendation: Save it somewhere to the your operating system's __Desktop__. Yes, that means anyone who takes over your laptop and notices a file named "`my_super_secret_creds.json`" on the Desktop now has access to your (secondary) account. But that's a (temporary) risk we'll take, and one that is __far preferable__ to the more common error: saving the file to your Github repo and committing the creds for the entire world to see.

So save the file to the Desktop (via your text editor), and for the purposes of this exercise, just name it `tw.json`.

### Accessing your Twitter creds file from another script

Now open up a brand new command-prompt window, and run `ipython` to start a new iPython session.

Then paste the following code:

~~~py
import json
import os
import tweepy
# Note this only works on OS X/Unix systems:
credspath = os.path.expanduser("~/Desktop/tw.json")
rawcreds = open(credspath).read()
mycreds = json.loads(rawcreds)
# Now mycreds is back to being a dictionary object
# We can re-run the tweepy code to get a new instance of the API object
t_auth = tweepy.OAuthHandler(
             consumer_key = mycreds['consumer_key'],
             consumer_secret = mycreds['consumer_secret']
)
t_auth.set_access_token(
      mycreds['access_token'],
      mycreds['access_token_secret']
)
the_api = tweepy.API(t_auth)
tme = the_api.me()
print("I've reauthenticated as screen_name:", tme.screen_name)
~~~

It should work as it did in the previous iPython instance. Congratulations, you now have a re-usable credentials file and you're now 90% on your way to easy, reproducible access to Twitter's API. What's next to do? Well, for starters, you can figure out a better place to store that credentials file that is not your Desktop (or a file folder that will accidentally get published to Github repo). It's those little details that can be the most painful...


### So you screwed up and exposed your credentials

It happens to everyone. You accidentally saved your credentials file to one of your file folders that you then pushed to Github. And now anyone in the world can copy that file and re-run the code we've used to control your bot. Mistakes happen. This one is easily fixable, and goes to the root of why we go through this whole OAuth process instead of creating a program in which we enter our Twitter usernames and passwords.

__If you believe you've exposed your credentials file__, open the browser in which you're logged in as your __main account__, visit [https://apps.twitter.com](https://apps.twitter.com), find the app that you used for the authentication process.

Then click the __Regenerate Consumer Key and Secret__ button.

You'll have to go through the whole authentication-via-opening-two-browsers process. But that's a whole lot better than having one of your password combinations (because let's face it, you probably re-used one of your personal passwords, which means you have to change __all__ of your other accounts, Twitter and non-Twitter).








