from celery import Celery
from time import sleep

app = Celery('task', broker='redis://localhost:6379', backend='db+sqlite:///db.sqlite3')


@app.task
def reverse(text):
    sleep(0.5)
    return text[::-1]

# celery -A tasks worker --loglevel=info
