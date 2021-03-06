import tweepy, os, time
import lib.stream as stream

if os.environ["bot_env"] == 'development':
     from credentials import keys

if __name__ == '__main__':
    os.system('clear')

    auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'])
    auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_SECRET'])

    search_terms = ['need a tutor', 'A-levels']

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5, timeout=60)
    streamListener = stream.Stream(api)
    stream = tweepy.Stream(auth=api.auth, listener=streamListener)

    stream.filter(languages=["en"], track=search_terms, async=True)
