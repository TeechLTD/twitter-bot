import tweepy

config = configparser.ConfigParser()
config = config.read('config.ini')
 = config['twitter']

auth = tweepy.OAuthHandler(config['CONSUMER_KEY'], config['CONSUMER_SECRET'])
auth.set_access_token(config['ACCESS_TOKEN'], config['ACCESS_SECRET'])
