import tweepy, json, os

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_SECRET'])
bot = tweepy.API(auth)

bot.update_status('www.getaderal.com')

print "success"
