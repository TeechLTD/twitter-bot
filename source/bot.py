import tweepy, json, os

if os.environ["bot_env"] == 'development':
     import credentials

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_SECRET'])
bot = tweepy.API(auth)

def duplicate():


    return;

def tweet():
    from tweets import tweet_list

    for tweet in tweet_list:
        bot.upda
    return;



tweet()




print "done"
