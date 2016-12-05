import tweepy
from processor import act_on, display_tweet, direct_message_new_followers

class Stream(tweepy.StreamListener):

    def __init__(self, api_instance):
        self.api = api_instance

        print("Listening...")
        print("Press ctrl-shift-/ to interrupt \n")

    def on_status(self, status):
        #display_tweet(status, self.api)
        act_on(status, self.api)

    def on_error(self, status_code):
        if status_code is 420:
            return False
        elif status_code is 403:
            return False
        elif status_code is 429:
            return False
        elif status_code is 502:
            sleep(120)
            return False
        elif status_code is 503:
            sleep(120)
            return False
        elif status_code is 504:
            sleep(120)
            return False
        else:
            print(status)
            time.sleep(120)
            return False
