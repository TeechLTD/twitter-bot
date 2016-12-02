import tweepy
from processor import act_on, display_tweet

class Stream(tweepy.StreamListener):

    def __init__(self, api_instance):
        self.api = api_instance

    def on_status(self, status):
        act_on(status, self.api)

    def on_error(self, status):
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
