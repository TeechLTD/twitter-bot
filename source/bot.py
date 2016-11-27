import tweepy, os, json

if os.environ["bot_env"] == 'development':
     import credentials

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        get_tweet(status)



def get_tweet(tweet):
    print("Tweet Message : " + tweet.text + "\n")



if __name__ == '__main__':
    auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
    auth.secure = True
    auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_SECRET'])

    bot = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5)

    streamListener  = StreamListener()
    myStream = tweepy.Stream(auth=bot.auth, listener=streamListener)

    myStream.filter(track=['adderall'], async=True)

print "\n done"
