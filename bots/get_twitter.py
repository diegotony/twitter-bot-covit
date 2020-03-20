import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def get_last_tweet(api):
    t = api.user_timeline(id = "Salud_Ec", count = 1)[0] 
    print(t.text) 

def main():
    api = create_api()
    while True:
        get_last_tweet(api)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()