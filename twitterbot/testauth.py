import json
import os
import tweepy
# Note this only works on OS X/Unix systems:
credspath = os.path.expanduser("~/Desktop/tw.json")
rawcreds = open(credspath).read()
mycreds = json.loads(rawcreds)
# Now mycreds is back to being a dictionary object
# We can re-run the tweepy code to get a new instance of the API object
t_auth = tweepy.OAuthHandler(
             consumer_key = mycreds['consumer_key'],
             consumer_secret = mycreds['consumer_secret']
)
t_auth.set_access_token(
      mycreds['access_token'],
      mycreds['access_token_secret']
)
the_api = tweepy.API(t_auth)
tme = the_api.me()
print("I've reauthenticated as screen_name:", tme.screen_name)

