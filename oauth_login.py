import twitter

def oauth_login():
    CONSUMER_KEY='Your Consumer Key'
    CONSUMER_SECRET='Your Consumer Secret'
    OAUTH_TOKEN='Your Oauth_Token'
    OAUTH_TOKEN_SECRET='Your OAuth_Token_secret'

    auth=twitter.oauth.OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
    
    twitter_api=twitter.Twitter(auth=auth)

    return twitter_api

twitter_api=oauth_login()

print twitter_api
