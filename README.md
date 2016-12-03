## Twitter marketing bot

A stream bot and collection of tools to automate twitter activity.

To use, ask me for the credentials, clone the repo and create a virtual environment

- Execute `bot.py` to run the streaming bot
- Associated tools are under `utilities`, there is a script to unfollow people who do not follow back, `unfollower.py`, one to get relevant stats on our account, `stats.py` and finally one to follow all the followers of a particular (or a couple of) twitter accounts, `follower.py`

### Warnings
  - Don't run all the scripts at once, it's likely twitter will put us in time out.
  - The number of requests we can make gets reset every 15min, so keep that in mind
