import tweepy
import logging
import time
from config import create_api
from api_covid import post_noticias
from twitter import get_last_tweet, auth_twitter
from listener import Listener
import os



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
listener = Listener()


def main():
    api = create_api()
    while True:


        t = get_last_tweet(api)
        urls = t.retweeted_status.entities['urls']
        # print(urls)
        url = ""
        for i in urls:
            url = i['url']

        noticia = {
            "fuente": url,
            "resumen": t.retweeted_status.text,
            "titulo": t.text
        }

        print(noticia)
        # post_noticias(noticia)

        logger.info("Waiting...")
        time.sleep(3600)


if __name__ == "__main__":
    main()
