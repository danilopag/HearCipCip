import pandas as pd
import numpy as np

from io import StringIO
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
from tweepy.error import RateLimitError, TweepError

data = pd.read_csv("TweetTest", ",")

from sklearn.feature_extraction.text import CountVectorizer

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

msglist=[]
i=0
correctCount=0 #contatore tweet indovinati
tweetCount=0 #contatore tweer analizzati

X=data["Tweet"]
print(X)
y = data["Politico"]
print(y)

ordered_class_list= list(set(y))
ordered_class_list.sort()
#print(ordered_class_list)
vectorizer_train = CountVectorizer(min_df=0, binary=True)
# min_df=0 significa "considerare tutti i token, anche se compaiono una sola volta"
vectorizer_train.fit(X)
x_train_array = vectorizer_train.transform(X).toarray()
#print(x_train_array)
#print("VECTOR TOKENS")
#print(vectorizer_train.get_feature_names())
#Fine Allenamento
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(x_train_array, y)
for tweet in Cursor(api.user_timeline, id="luigidimaio").items(800):
        i+=1
        if i > 700:
            msglist.append(str(tweet.text))
        
#msg_array = vectorizer_train.transform((msglist[0])).toarray()
#print(msg_array) #Stampa Array Binario
#class_probabilities = clf.predict_proba(msg_array)[0]
#prova = list(zip(ordered_class_list, class_probabilities))
#for i in prova:
#    print('{} : {}'.format(i[0], i[1]))
#print(clf.predict(msg_array))
for msg in msglist:
        tweetCount+=1
        #print("\n\n MSG: ", msg)
        msg_array = vectorizer_train.transform([msg]).toarray()
        #print("MSG tokens : ", msg.split())
        #print("MSG array repr: ", msg_array)

        #calcolo confidence per classe
        #il risultato è una lista di float in ordine alfabetico per classe
        class_probabilities = clf.predict_proba(msg_array)[0]
        class_confidence = list(zip(ordered_class_list, class_probabilities))
        #for c in class_confidence:
        #    print("{} : {:.3f} %".format(c[0].ljust(10), c[1]))
        r = clf.predict(msg_array)
        print("PREDICTED CLASS :", r[0])
        if (r[0] == "LuigiDiMaio"):
            correctCount+=1
        if (tweetCount == 5 or tweetCount == 10 or tweetCount == 50 or tweetCount == 100):
            percCorrezione= (correctCount/tweetCount)*100
            print("Predizioni indovinate: ", correctCount)
            print("Percentuale: {:.3f} %".format(percCorrezione))




