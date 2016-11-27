# -*- coding: utf-8 -*-

import tweepy, os, time

if os.environ["bot_env"] == 'development':
     from credentials import keys

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        # display_tweet(status)
        act_on_tweet(status)

    def on_error(self, status):
        if status_code == 420:
            return False
        elif status_code == 403:
            return False
        elif status_code == 429:
            return False
        else:
            wait_a_minute
            return True

def display_tweet(tweet):
    print("Tweet Message : " + tweet.text)
    print("Tweet id : " + str(tweet.id))
    print("Tweet user : " + tweet.user.name)
    print("Tweet user id : " + str(tweet.user.id) + "\n")
    friendship = bot.show_friendship(target_id=tweet.user.id)
    print friendship[1].followed_by

def act_on_tweet(tweet):
    tweet_id = tweet.id
    user = tweet.user

    frienship = bot.show_friendship(target_id=tweet.user.id)
    friends = friendship[1].followed_by

    try:
        bot.create_favorite(tweet_id)
        print("favorited a tweet by: " + str(user.name) + "\n")
    except:
        print("favoriting a tweet by: " + str(user.name) + "failed! \n" )
        pass

    wait_a_minute

    # follow if user does not follow us
    if friends:
        if "@aderalv2" in tweet.text:
            try:
                bot.retweet(tweet_id)
                reply(tweet_id, user.name)
            except:
                print("replying to:" + str(user.name) + "failed! \n" )
    else:
        bot.create_friendship(user.id, bot_id)

    wait_a_minute

def reply(tweet_id, user_name):
    reply = "@%s, we are listening. Join our community today to boost your potential." % (user_name)
    try:
        bot.update_status(reply, tweet_id)
        print("Retweeted and replied to: " + str(user.name) + "\n")
        wait_a_minute
    except:
        print("reply to: " + str(user.name) + "failed! \n" )
        pass


def direct_message(user):
    message = "@%s, welcome to our world. То learn more about us and check on availabilities - follow the link in our bio." % (user.name)
    try:
        bot.send_direct_message(user.id)
        print("sent a direct message to: " + str(user.name) + "\n")
    except:
        print("direct message to: " + str(user.name) + "failed! \n" )
        pass
    wait_a_minute

def unfollow(user_list):
    # TODO
    return None

# prevent excessive spamming
def wait_a_minute():
    sleep(20)

if __name__ == '__main__':

    auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'])
    auth.secure = True
    auth.set_access_token(keys['ACCESS_TOKEN'], keys['ACCESS_SECRET'])

    bot = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5)
    streamListener = StreamListener()
    myStream = tweepy.Stream(auth=bot.auth, listener=streamListener)

    bot_id = bot.get_user("aderalv2").id
    # TODO: add a cursor here
    bot_followers = bot.followers(bot_id)

    search_terms = ["adderal", "aderal", "adderral", "I need adderall", '@aderalv2', 'getaderal.com', 'education']
    myStream.filter(languages=["en"], track=search_terms, async=True)

print "Fetching..... \n"
