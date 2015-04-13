---
title: Introduction to IFTTT
---

[IFTTT](https://ifttt.com/), short for, "If this, then that" purports to let you "put the Internet to work for you."

Sign up for IFTTT and try installing a recipe to get an idea of how the process works and the steps involved. For your actual project, you might find it worthwhile to implement your own kind of custom "if this do that" recipe. The [Zapier service is very similar to IFTTT](https://zapier.com/) except with a lot more flexibility (with the tradeoff of simplicity).


## Sample recipe: Instagram to Twitter


If you're on Twitter and Instagram, a useful recipe involves linking the two accounts together, so that posting a photo on Instagram will also post it to your Twitter account.

By default, if you have Instagram post to your Twitter account, it will look like this:

![img](/files/images/tutorials/apis/instagram-twitter-non-integration.png)

But Twitter has the ability to embed photos. And they make the Tweet look much nicer:

<blockquote class="twitter-tweet" lang="en"><p><a href="https://twitter.com/dancow">@dancow</a> what is that a kale tortilla, hippy?</p>&mdash; djkilllist (@djkilllist) <a href="https://twitter.com/djkilllist/status/585821920911691776">April 8, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

But to do that, these are the steps you'd have to go through:

1. Take a photo
2. Open the Instagram App
3. Upload the photo to Instagram
4. Publish the photo to Instagram (with caption and such)
5. Go to the Twitter App
6. Upload the Instagram photo (from your mobile device's photo albums)
7. Retype the caption
8. Paste a link to the Instagram web photo 
9. Publish the tweet

With all those steps, it's no wonder that few people actually do it. Not even billionaires:

<blockquote class="twitter-tweet" lang="en"><p>😎🐰 <a href="https://twitter.com/hashtag/HappyEaster?src=hash">#HappyEaster</a> <a href="https://t.co/NaYUJ183aI">https://t.co/NaYUJ183aI</a></p>&mdash; Paris Hilton (@ParisHilton) <a href="https://twitter.com/ParisHilton/status/584922499172982784">April 6, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


## Create a recipe

Go to the [Create a Recipe](https://ifttt.com/myrecipes/personal/new) page.

The first step is to __choose a "Trigger Channel"__; this is the service that you want to create a _reaction_ to. If you want a Tweet to be sent out after a photo is posted to Instagram, the "Trigger Channel" is __Instagram__.

![img](/files/images/tutorials/apis/ifttt-choose-trigger-channel.png)

At this point, you'll be asked to authorize IFTTT to have access to your Instagram account:

![img](/files/images/tutorials/apis/ifttt-authorize-instagram.png)


There's more than one trigger for Instagram, choose the first one: __Any photo by you__:

![img](/files/images/tutorials/apis/ifttt-choose-instagram-trigger.png)

IFTTT will then prompt you to choose an __"Action Channel"__, in this case, Twitter. Choose __Post a tweet with image__: 

> This Action will post a new tweet to your Twitter account with a linked pic.twitter.com image.

![img](/files/images/tutorials/apis/ifttt-choose-twitter-action.png)



#### Customize the action

By default, this recipe is set up to tweet the text of the __Caption__ you've made for the Instagram photo. The __Image URL__ field will be filled by the __SourceUrl__ for the Instagram photo. 

Let's add one more "ingredient" to body of the Tweet: the __URL__ to the Instagram photo page, so that people can get to the originating Instagram account.

![img](/files/images/tutorials/apis/ifttt-choose-twitter-action-fields.png)

You can add other ingredients or boilerplate text to the tweet, such as: "Follow me on Instagram". 

![img](/files/images/tutorials/apis/ifttt-create-action.png)


When you're done, click __Create Action.__



---



### Background information


Why don't services let you do what you want?


[Twitter CEO says Instagram removing cards support was 'their prerogative'
](http://www.theverge.com/2012/12/5/3730876/instagram-cuts-off-twitter-cards-integration-further-souring-relationship)


[Instagram documentation on Media Endpoints](https://instagram.com/developer/endpoints/media/):

> At this time, uploading via the API is not possible. We made a conscious choice not to add this for the following reasons:
>
> Instagram is about your life on the go – we hope to encourage photos from within the app.
> We want to fight spam & low quality photos. Once we allow uploading from other sources, it's harder to control what comes into the Instagram ecosystem. 
> All this being said, we're working on ways to ensure users have a consistent and high-quality experience on our platform.


### Effect of embedded photos on Twitter

[What fuels a Tweet's engagement?](https://blog.twitter.com/2014/what-fuels-a-tweets-engagement)

![img](/files/images/tutorials/apis/effect-on-retweets.png)
