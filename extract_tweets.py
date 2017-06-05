import twitter
import json
#prevent url encoding errors in next_results
from urllib.parse import unquote

from twitter_keys import getTwitterAccess

auth=getTwitterAccess()

twitter_api=twitter.Twitter(auth=auth)


q='#Python3'

count=100


search_results=twitter_api.search.tweets(q=q,count=count)


statuses=search_results['statuses']

status_texts=[status['text'] for status in statuses]

screen_names=[ user_mention['screen_name'] for status in statuses for user_mention in status['entities']['user_mentions']]

hashtags=[hashtag['text'] for status in statuses for hashtag in status['entities']['hashtags']]




words = [ w for t in status_texts for w in t.split()]



print(json.dumps(status_texts[0:5],indent=1))

print(json.dumps(screen_names[0:5],indent=1))
print(json.dumps(hashtags[0:5],indent=1))

print(json.dumps(words[0:5],indent=1))
