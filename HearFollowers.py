import csv
import sys

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
from tweepy.error import RateLimitError, TweepError

from datetime import datetime


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
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#Print last 20 Followers
user = api.get_user("lucamariano17")

print("USER Details: \n")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 Followers")
for follower in user.followers():
    print(follower.name)
    print(follower.description)
#Tendenza Hashtag #primagliitaliani
for tweet in api.search(q="#primagliitaliani", lang="it", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")

#Print last 50 tweets
for tweet in Cursor(api.user_timeline, id="lucamariano17").items(20):
    print(f"{tweet.user.name} said: {tweet.text}")
