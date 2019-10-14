from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)


# CORS(app)


@app.route('/api')
@cross_origin()
def api():
    # return jsonify({'data': 'Hello World!'})
    return {'data': 'Hello World!'}  # Since Flask 1.1 you don't need jsonify, a simple dictionary will work just fine


if __name__ == '__main__':
    app.run()
