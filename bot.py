import tweepy, os, time, sys
import lib.streamListener

if os.environ["bot_env"] == 'development':
     from credentials import keys

if __name__ == '__main__':

    os.system('clear')

    auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'])
    auth.secure = True
    auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_SECRET'])

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5, timeout=60)
    streamListener = StreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=streamListener)

    search_terms = ["adderal", "aderal", "adderral", "I need adderall", '@aderalv2', 'getaderal.com', 'need a tutor', 'A-levels']

    myStream.filter(languages=["en"], track=search_terms, async=True)
