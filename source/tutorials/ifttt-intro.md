---
title: Introduction to IFTTT
---

[IFTTT](https://ifttt.com/), short for, "If this, then that" purports to let you "put the Internet to work for you."


## Sample recipe: Instagram to Twitter


![img](/files/images/tutorials/apis/instagram-twitter-non-integration.png)

- [Instagram](https://instagram.com/p/1MopAkwi9n/)
- [Twitter](https://twitter.com/dancow/status/585632387398238208)




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

Why don't services let you do what you want?

http://www.nytimes.com/2015/04/08/us/ferguson-adds-blacks-to-city-council-but-rejects-activist-candidates.html
[Twitter CEO says Instagram removing cards support was 'their prerogative'
](http://www.theverge.com/2012/12/5/3730876/instagram-cuts-off-twitter-cards-integration-further-souring-relationship)


[Instagram documentation on Media Endpoints](https://instagram.com/developer/endpoints/media/):

> At this time, uploading via the API is not possible. We made a conscious choice not to add this for the following reasons:
>
> Instagram is about your life on the go – we hope to encourage photos from within the app.
> We want to fight spam & low quality photos. Once we allow uploading from other sources, it's harder to control what comes into the Instagram ecosystem. 
> All this being said, we're working on ways to ensure users have a consistent and high-quality experience on our platform.
