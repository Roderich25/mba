import redis

CHANNEL = "PubSubChannel"

if __name__ == '__main__':
    client = redis.StrictRedis(
        host='localhost',
        port=6379,
        db=0
    )

    subscription = client.pubsub()
    subscription.subscribe(CHANNEL)
    print("Waiting messages...")

    while True:

        message = subscription.get_message()

        if message and message.get('data', False) and not message['data'] == 1:
            print(message['data'].decode())
