import tweepy, json, os
import credentials

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_SECRET'])
bot = tweepy.API(auth)

def tweet():
    with open('tweets.txt','r') as f:
        line = f.readline()
        print(line.rstrip('\n'))
        print
        lines = f.readlines()

    for line in lines:
        print(line.rstrip('\n'))

    return;

tweet()








print "done"
