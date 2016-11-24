import tweepy
import json
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

bot = tweepy.API(auth)

bot.update_status('ready to rock')


print "success"
