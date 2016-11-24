import tweepy, configparser


config = configparser.ConfigParser()
config = config.read('config.ini')
config = config['twitter']

auth = tweepy.OAuthHandler(config['CONSUMER_KEY'], ['CONSUMER_SECRET'])
auth.set_access_token(config['ACCESS_TOKEN'],['ACCESS_SECRET'])
