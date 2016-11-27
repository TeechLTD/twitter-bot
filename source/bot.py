import tweepy, os, time
from tweets import replies, message

if os.environ["bot_env"] == 'development':
     from credentials import keys

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        get_tweet(status)
        # act_on_tweet(status)

    def on_error(self, status):
        if status_code == 420:
            return False
        elif status_code == 403:
            return False
        elif status_code == 429:
            return False
        else:
            time.sleep(15)
            return True

def get_tweet(tweet):
    print("Tweet Message : " + tweet.text)
    print("Tweet id : " + str(tweet.id))
    print("Tweet user : " + tweet.user.name)
    print("Tweet user : " + str(tweet.user.id) + "\n")

def act_on_tweet(tweet):
    id = tweet.id
    bot.create_favorite(id)
    sleep(60)
    return;

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'])
    auth.secure = True
    auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_SECRET'])

    bot = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5)


    bot.update_status("Back")
    streamListener  = StreamListener()
    myStream = tweepy.Stream(auth=bot.auth, listener=streamListener)

    search_terms = ["adderal", "aderal", "adderral", "I need adderall", "Education", "need a tutor"]

    myStream.filter(track=search_terms, async=True)



print "Fetching..... \n"
