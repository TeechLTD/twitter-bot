# Twitter limits : 3200 tweets, 200 at a time  (15min interval)

import tweepy, json, os, datetime

if os.environ["bot_env"] == 'development':
     import credentials

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_SECRET'])
bot = tweepy.API(auth, monitor_rate_limit=True, wait_on_rate_limit=True)


def tweet():
    from tweets import tweet_list
    #method to tweet from premade list
    return;

def search(parameter):
    #fetch user list by parameters
    return;


print "done"
