import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
from tweepy.error import RateLimitError, TweepError


class MyStreamListener(StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print("INIZIO TWEET")
        print(f"{tweet.user.name}:{tweet.text}\n")
        print("FINE TWEET")

    def on_error(self, status):
        print("Error detected")

d = {
"consumer_key": "",
"consumer_secret": "",
"access_token": "",
"access_token_secret": ""
}

# Authenticate to Twitter
auth = OAuthHandler(d["consumer_key"], d['consumer_secret'])
auth.set_access_token(d['access_token'], d['access_token_secret'])
#Create API object
api = API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

tweets_listener = MyStreamListener(api)
stream = Stream(api.auth, tweets_listener)
stream.filter(track=["Univeti", "@univeti"], languages=["it"])
