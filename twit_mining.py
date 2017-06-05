import twitter
import json

from twitter_keys import getTwitterAccess

auth=getTwitterAccess()
twitter_api=twitter.Twitter(auth=auth)


#print(twitter_api)



#twiiter uses yahoo where on earth id
WORLD_WOE_ID=1
US_WOE_ID=23424977


world_trend=twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trend=twitter_api.trends.place(_id=US_WOE_ID)


#print(world_trend)

#print()
#print(us_trend)


for trend in world_trend[0]['trends']:
	print(trend['name'])



for trend in us_trend[0]['trends']:
	print(trend['name'])


world_trend_set=set([trend['name'] for trend in world_trend[0]['trends']])


us_trend_set=set([trend['name'] for trend in us_trend[0]['trends']])


common_trends=world_trend_set.intersection(us_trend_set)

print(common_trends)
