import tweepy, os, time
import lib.stream as stream

if os.environ["bot_env"] == 'development':
     from credentials import keys

if __name__ == '__main__':
    os.system('clear')

    auth = tweepy.OAuthHandler(keys['TEECH_CONSUMER_KEY'], keys['TEECH_CONSUMER_SECRET'])
    auth.set_TEECH_ACCESS_TOKEN(keys['TEECH_ACCESS_TOKEN'], keys['TEECH_ACCESS_SECRET'])

    start_time = time.time()
    search_terms = ['@TeechGlobal', 'need a tutor', 'A-levels', 'gsce','help with calculus', 'homework help', 'homework']

    print("Tracking: " + str(search_terms) + "\n")

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5, timeout=60)
    streamListener = stream.Stream(api)
    stream = tweepy.Stream(auth=api.auth, listener=streamListener)

    stream.filter(languages=["en"], track=search_terms, async=True)
