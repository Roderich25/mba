from os import getenv
import json
from TwitterAPI import TwitterAPI

consumer_key = getenv('API_KEY')
consumer_secret = getenv('API_SECRET_KEY')
access_token_key = getenv('ACCESS_TOKEN')
access_token_secret = getenv('ACCESS_TOKEN_SECRET')
# print((consumer_key, consumer_secret, access_token_key, access_token_secret))
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

r = api.request('statuses/show/:%d' % 1278380283918598144)
# print(r.text)
# print(dir(r))
payload = json.loads(r.text)
print(json.dumps(payload, indent=4, sort_keys=True))
