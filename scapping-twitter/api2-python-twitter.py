from os import getenv
import twitter

consumer_key = getenv('API_KEY')
consumer_secret = getenv('API_SECRET_KEY')
access_token_key = getenv('ACCESS_TOKEN')
access_token_secret = getenv('ACCESS_TOKEN_SECRET')

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)

statuses = api.GetUserTimeline(screen_name="ConacytYa")
# print([s.text for s in statuses])
for status in statuses:
    print(status)


users = api.GetFriends()
# print([u.name for u in users])
for user in users:
    print(user)

