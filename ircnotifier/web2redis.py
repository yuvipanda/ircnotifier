import json
from flask import Flask, request
from redis import StrictRedis

app = Flask(__name__)
redis = StrictRedis()

@app.route('/v1/send', methods=['POST'])
def send():
    # Validate, validate, validate!
    if not 'message' in request.form:
        return 'No message found', 400
    if not 'channels' in request.form:
        return 'No channels found', 400
    if not 'token' in request.form:
        return 'No token found', 400
    data = {
        'message': request.form['message'],
        'channels': request.form.getlist('channels')
    }
    redis.rpush('ircnotifier', json.dumps(data))
    return repr(data)

if __name__ == '__main__':
    app.run(debug=True)