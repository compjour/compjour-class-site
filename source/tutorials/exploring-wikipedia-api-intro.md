# Exploring the Wikipedia JSON API

The documentation to the Mediawiki API (which is what Wikipedia runs off of) is here: [http://www.mediawiki.org/wiki/API:Main_page](http://www.mediawiki.org/wiki/API:Main_page). The following is an abbreviated introduction with Python examples.

Our objective is to get data about any given Wikipedia page, such as [Stanford University](http://en.wikipedia.org/wiki/Stanford_University), in a more machine-readable format than HTML. Things we are interested in knowing are: what's on the page, how big is it, who/what/when/where/why users have been editing it.

## The Query Module

The Mediawiki API has many functions and endpoints beyond just reading data; for example, there are [many Wikipedia bots](http://en.wikipedia.org/wiki/Wikipedia:Bots) for the automating of article edits. But we only care about _reading_, or __getting__ the data. And for that, [there's the __Query Module__](https://www.mediawiki.org/wiki/API:Query), which "allows you to get most of the data stored in a wiki, such as the wikitext of a particular article."

__Sidenote__: Here's a fun example of a semi-autonomous bot, in which the owner queries for a particular phrase and then has to hand-edit it himself : [One Man’s Quest to Rid Wikipedia of Exactly One Grammatical Mistake](http://news.slashdot.org/story/15/02/03/182201/one-mans-quest-to-rid-wikipedia-of-exactly-one-grammatical-mistake)

The Query module itself has an extensive list of submodules. For now, we care about the [__Property__-type of queries](https://www.mediawiki.org/wiki/API:Properties), which allows us to "_get various data about a list of pages specified with either the titles=, pageids=, or revids= parameters._"

And here are the kinds of __property__ queries that are interesting to us right now:

- [info](https://www.mediawiki.org/wiki/API:Info) - basic information about a page, including its unique ID, canonical title, last revision, size, and number of "watchers."
- [revisions](https://www.mediawiki.org/wiki/API:Revisions) - a list of changes/edits made to a page.


--------------

## Testing out the API via Browser

http://en.wikipedia.org/w/api.php?action=query&prop=info&titles=Stanford_University



Getting the raw data:

http://en.wikipedia.org/w/api.php?action=query&prop=info&format=json&titles=Stanford_University

------------

## The components of a HTTP Call:

#### The base endpoint

     http://en.wikipedia.org/w/api.php?

#### The parameters

These are _required_ for :

- `action=query`
- `prop=info`
- `format=json`

These are conditional:

`titles=Stanford_University`

#### Getting more than one title

`titles=Stanford_University|Harvard_University`


#### Getting extra attributes with `in_prop`

- `protection`: The protection level 
- `watchers`: The number of watchers

http://en.wikipedia.org/w/api.php?action=query&prop=info&titles=Stanford_University&inprop=protection|watchers




### Extracts 

[prop=extracts](http://www.mediawiki.org/wiki/Extension:TextExtracts#API)


