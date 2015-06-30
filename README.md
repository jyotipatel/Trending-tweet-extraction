# Trending-tweet-extraction

This code extracts trending tweets from twitter using OAuth. you have to register an application under your Twitter account at http://dev.twitter.com/apps and take note of consumer key ,consumer secret, access token and access token secret.

#oauth_login.py
Enables you to use twitter package benefits (nothing to display)

#extract.py
Extracts trending tweets using your credentials , it makes use of WOE_ID (http://woeid.rosselliot.co.nz/lookup) for tweets from different geographical regions.

#savemongo.py
Saves the tweets obtained in mongodb.
