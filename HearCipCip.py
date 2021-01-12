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

#Ricerca 
f = open("TweetTest", 'w', encoding='utf-8')
try:
    writer = csv.writer(f)
    print("TWEET")
    writer.writerow(("Tweet","Politico"))
    for tweet in Cursor(api.user_timeline, id="matteorenzi").items(1000):
        #date_time = tweet.created_at.strftime("%m/%d/%Y, %H:%M:%S")
        #print("Data e orario:",date_time)
        #print("TESTO: " + tweet.text)
        writer.writerow((tweet.text,"MatteoRenzi"))
    for tweet in Cursor(api.user_timeline, id="matteosalvinimi").items(1000):
        #date_time = tweet.created_at.strftime("%m/%d/%Y, %H:%M:%S")
        #print("Data e orario:",date_time)
        #print("TESTO: " + tweet.text)
        writer.writerow((tweet.text,"MatteoSalvini"))
    for tweet in Cursor(api.user_timeline, id="luigidimaio").items(1000):
        #date_time = tweet.created_at.strftime("%m/%d/%Y, %H:%M:%S")
        #print("Data e orario:",date_time)
        #print("TESTO: " + tweet.text)
        writer.writerow((tweet.text,"LuigiDiMaio"))
    for tweet in Cursor(api.user_timeline, id="GiorgiaMeloni").items(1000):
        #date_time = tweet.created_at.strftime("%m/%d/%Y, %H:%M:%S")
        #print("Data e orario:",date_time)
        #print("TESTO: " + tweet.text)
        writer.writerow((tweet.text,"GiorgiaMeloni"))
finally:
    f.close()
