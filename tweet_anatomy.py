import twitter
import json
#prevent url encoding errors in next_results
from urllib.parse import unquote

from twitter_keys import getTwitterAccess

auth=getTwitterAccess()
twitter_api=twitter.Twitter(auth=auth)


q='#MothersDay'

count=100


search_results=twitter_api.search.tweets(q=q,count=count)


statuses=search_results['statuses']

for _ in range(5):
    print('length of statuses',len(statuses))
    try:
        next_results=search_results['search_metadata']['next_results']
    except KeyError as e:
        break


    kwargs=dict([kv.split('=') for kv in unquote(next_results[1:]).split("&")])

    search_results=twitter_api.search.tweets(**kwargs)
    statuses +=search_results['statuses']



print(json.dumps(statuses[0],indent=1))




for i in range(10):
    print()
    print(statuses[i]['text'])
    print('favorites:',statuses[i]['favorite_count'])
    print('Retweets:',statuses[i]['retweet_count'])
