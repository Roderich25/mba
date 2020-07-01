from os import getenv
import tweepy


consumer_key = getenv('API_KEY')
consumer_secret = getenv('API_SECRET_KEY')
access_token_key = getenv('ACCESS_TOKEN')
access_token_secret = getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

user = api.get_user('ConacytYa')
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
    print(friend.screen_name)

