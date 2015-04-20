By Dan Nguyen

# Pitch

Everyone who tweets at my bot with an address and the hashtag `#showme` will be tweeted back the most interesting recent Instagram photo near that address.

For example, a Tweet that looks like this:

        @samplebot #showme Tokyo, Japan

&ndash; will respond with:

        @user Here's an interesting photo near Tokyo, Japan [instagramlink]


# The steps

1. Bot checks Twitter API endpoint of [statuses/mentions_timeline](https://dev.twitter.com/rest/reference/get/statuses/mentions_timeline)
2. For each Tweet, the bot to see if the #showme hashtag was used. Also, note the user's screen name and the ID of the tag.
3. Getting the location: The location to look up is either the other text in that tweet. Or, if the tweet has geolocation enabled, we use those coordinates.
4. If the location is an address string, use the [Google Maps geocoding API to get lat/lng coordinates](https://developers.google.com/maps/documentation/geocoding/).
5. Use Instagram's [media/search](https://instagram.com/developer/endpoints/media/?hl=en#get_media_search) endpoint and pass in the lat/lng coordinates.
6. From Instagram's request, choose the highest photo based on number of Likes.
7. Extract the image's web link
8. Use Twitter's [statuses/update](https://dev.twitter.com/rest/reference/post/statuses/update) endpoint and reply back to the user with the Instagram URL.





