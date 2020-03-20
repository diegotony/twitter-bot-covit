import tweepy


def auth_twitter(key, secret):
    return tweepy.OAuthHandler(key, secret)


def access_token(auth, token, secret):
    return auth.set_access_token(token, secret)


def get_last_tweet(api):
    t = api.user_timeline(id="Salud_Ec", count=1)[0]
    return t
