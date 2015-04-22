# YoloBroBot README

A rip-off of ["Bro" from Silicon Valley S2E2](http://www.businessinsider.com/silicon-valley-built-bro-app-2015-4)

## Pitch

Everytime someone tweets at the bot with the hashtag "#bro", reply back with:

> @theuser #YOLOBRO
> 


## Steps

From the bot's perspective:

#### 1. Get my latest tweets

#### 2. From my latest tweets, find the most recent one in which I replied to someone with the "#YOLOBRO" hashtag. 

If no such tweet exists, set a variable (`xid`) representing the last tweet ID to search from to 1. If such tweet does exist, use the value for `in_reply_to_status_id` 

#### 3. Get the most recent mentions of me since `xid`


#### 4. Of those mentions, find the first (oldest) instance of someone using the "#BRO" hashtag

#### 5. Formulate an appropriate response as a text string (i.e. '#YOLOBRO')

Should I say something more than "#YOLOBRO?"


#### 6. Reply back to that user (with that text string)


