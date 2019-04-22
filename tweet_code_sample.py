import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import StreamListener

access_token = "MY-ACCESS-TOKEN"
access_token_secret = "MY-ACCESS-TOKEN-SECRET"
consumer_key = "MY-CONSUMER-KEY"
consumer_secret = "MY-CONSUMBER-SECRET"

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#fetch recent 100 tweets containing words kardashiam, kanye, jenner
fetched_tweets = api.search(q=['kardashian','kanye','kendall jenner','kylie jenner'], result_type='recent', lang='en', count=100)
print("Number of tweets: {}".format(len(fetched_tweets)))
#----output----
# Number of tweets: 100

# print the tweet text
for tweet in fetched_tweets:
  print('Tweet ID: {}, Tweet Text: {}\n'.format(tweet.id, tweet.text))
