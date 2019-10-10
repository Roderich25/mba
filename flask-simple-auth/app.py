from flask import Flask
from flask_basicauth import BasicAuth

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'csat'
app.config['BASIC_AUTH_PASSWORD'] = 'csat'
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)


@app.route('/')
def home():
    return "home sweet home"


@app.route('/secret')
def secret():
    return "dont tell anyone"


@app.route('/hello')
def hello():
    return "hello darkness my old frined"


@app.route('/bye')
def bye():
    return "bye bye bye"


if __name__ == '__main__':
    app.run()
