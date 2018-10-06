#!/usr/bin/env python
# -*- coding: utf-8 -*-

from brainyquote import pybrainyquote
import tweepy, time

# API keys for Twitter
CONSUMER_KEY = '' 
CONSUMER_SECRET = '' 
ACCESS_KEY = '' 
ACCESS_SECRET = ''


# How many tweets should the bot make?
maxTweets = 1

# How long (in characters) can the tweet be?
maxLen = 128

# How long is the delay (in seconds) between tweets?
sleepTime = 10


# Setup API for use
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


# Tweet for `maxTweets` times (you can replace this with an infinite loop!)
for i in range(0, maxTweets):
    try:
        q = pybrainyquote.get_random_quote()
        if q:
            for r in q:
                quote = str(r)
                if len(quote) <= maxLen:
                    api.update_status(quote)
                    print(quote)
                    print("\n")
                    time.sleep(sleepTime)
                else:
                    q = pybrainyquote.get_random_quote()
    except tweepy.TweepError:
        q = pybrainyquote.get_random_quote()
        
