import json
import twitter
import oauth_login

def twitter_trends(twitter_api,woe_id):
    return twitter_api.trends.place(_id=woe_id)


#sample usage
twitter_api=oauth_login.oauth_login()
WORLD_WOE_ID =1
world_trends=twitter_trends(twitter_api,WORLD_WOE_ID)
print json.dumps(world_trends,indent=1)

INDIA_WOE_ID=23424848
trends=twitter_trends(twitter_api,INDIA_WOE_ID)
print json.dumps(trends,indent=1)

#WOE_ID can be obtained from "http://woeid.rosselliot.co.nz/lookup"
