import twitter
import json
from collections import Counter
#prevent url encoding errors in next_results
from urllib.parse import unquote

from twitter_keys import getTwitterAccess
from prettytable import PrettyTable



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

for item in [words,screen_names,hashtags]:
    c=Counter(item)
    print(c.most_common()[:10])
    print()



for label, data in (('Word',words),('Screen Name',screen_names),('Hashtag',hashtags)):
    pt=PrettyTable(field_names=[label,'Count'])
    c=Counter(data)
    [ pt.add_row(kv) for kv in c.most_common()[:10]]
    pt.align[label],pt.align['Count']='1','r'
    print(pt)




def lexical_diversity(tokens):
    return len(set(tokens))/len(tokens)


def average_words(statuses):
    total_words=sum([ len(s.split()) for s in statuses])
    return total_words/len(statuses)


print(lexical_diversity(words))

print(lexical_diversity(screen_names))

print(lexical_diversity(hashtags))


print(average_words(status_texts))

retweets=[(status['retweet_count'],status['retweeted_status']['user']['screen_name'],status['retweeted_status']['id'],status['text'])
            for status in statuses
                if 'retweeted_status' in status.keys()
          ]


pt=PrettyTable(field_names=['Count','Screen Name','Tweet ID','Text'])
[pt.add_row(row) for row in sorted(retweets,reverse=True)[:5]]
pt.max_width['Text']=50
pt.align='l'
print(pt)
