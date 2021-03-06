import tweepy
import logging
import os
from listener import Listener

consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

logger = logging.getLogger()



def create_api():

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    # try:
    #     api.verify_credentials()
    # except Exception as e:
    #     logger.error("Error creating API", exc_info=True)
    #     raise e
    # logger.info("API created")
    return api

def create_auth(track):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitterStream = tweepy.Stream(auth, Listener())
    return twitterStream.filter(track=[track])
