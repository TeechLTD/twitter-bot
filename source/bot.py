import tweepy, json, os

if os.environ["bot_env"] == 'development':
     import credentials

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_SECRET'])
bot = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,  retry_count=10, retry_delay=5, retry_errors=5))

def process_page(page):
    page[0]
    return;


# find people who tweet about aderal
# test on first 5 pages
for page in tweepy.Cursor(bot.search, q="aderal").pages(1):
    process_page(page)


# re-tweet their tweets
# start it for 10 followers




print "done"
