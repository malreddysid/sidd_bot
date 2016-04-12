#coding: utf-8

import tweepy
#from our keys module (keys.py), import the keys dictionary
from OAuthSettings import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

twts = api.search(q="recieve")
print "twts received"


for s in twts:
			sn = s.user.screen_name
			m = "@%s It's spelled receive my friend! :)" % (sn)
			print "Replying to " + sn
			s = api.update_status(m, s.id)
