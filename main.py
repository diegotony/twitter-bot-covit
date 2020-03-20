import tweepy
import requests


# Authenticate to Twitter
API_KEY = 'vSPcNTigMOpqhEtqowKJWtPzT'
API_SECRET = 'XXgB3sSjtSRTKZtiN6Y1v1XeqtM8mldamTWyTVY8FjLunjEom6'
ACCES_TOKEN = '211648785-TIZS8vYPZspSZp8uG0tG7H6NmYSg5GMt7UgGLn26'
ACCES_TOKEN_SECRET = '9BuLBSDgJ4dvX9TOlvb1Ik9Fm5uQ6nX4k8nNv7X9wmQIV'



auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCES_TOKEN, ACCES_TOKEN_SECRET)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


try:
    # for tweet in api.search(q="Covid", lang="es", rpp=10):
    #     print(f"{tweet.user.name}:{tweet.text}")
    t = api.user_timeline(id = "Salud_Ec", count = 1)[0] 
    print(t.text)       
except Exception as e:
    print(e)

