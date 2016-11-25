import tweepy, os, time

if os.environ["bot_env"] == 'development':
     import credentials

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_SECRET'])
bot = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5)

def process(list):
    # for tweet in list:
    #     tweet.user.create_friendship
    #     tweet
    return;


# find people who tweet about aderal
# test on first 5 pages
search_results = []
for page in tweepy.Cursor(bot.search, q="aderal", lang="en").pages(1):
    search_results.append(page)


process(search_results)


# re-tweet their tweets
# start it for 10 followers




print "done"
