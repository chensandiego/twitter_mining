import twitter
import json
#prevent url encoding errors in next_results
from urllib.parse import unquote

from twitter_keys import getTwitterAccess
import nltk

##download vader lexicon if it is not available
#nltk.download('vader_lexicon')
import numpy as np

from nltk.sentiment.vader import SentimentIntensityAnalyzer

auth=getTwitterAccess()
twitter_api=twitter.Twitter(auth=auth)
twitter_stream=twitter.TwitterStream(auth=auth)

iterator=twitter_stream.statuses.sample()

tweets=[]

for tweet in iterator:
    try:
        if tweet['lang']=='en':
            tweets.append(tweet)
    except:
        pass
    if len(tweets)==1000:
            break


analyzer=SentimentIntensityAnalyzer()
print(analyzer.polarity_scores('Hello'))
print(analyzer.polarity_scores('I really enjoy this video series'))

print(analyzer.polarity_scores('I REALLY enjoy this video series'))

scores=np.zeros(len(tweets))

for i,t in enumerate(tweets):
    text=t['text']

    polarity=analyzer.polarity_scores(text)
    scores[i]=polarity['compound']

most_positive=np.argmax(scores)
most_negative=np.argmin(scores)


print('{0:6.3f}: "{1}"'.format(scores[most_positive],tweets[most_positive]['text']))


print('{0:6.3f}: "{1}"'.format(scores[most_negative],tweets[most_negative]['text']))
