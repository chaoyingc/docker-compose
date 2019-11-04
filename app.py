import time
from redis import Redis
from flask import Flask, request, jsonify

app = Flask(__name__)
#cache = redis.Redis(host='redis', port=6379)
redis = Redis(host="redis", db=0, socket_timeout=5, charset="utf-8", decode_responses=True)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/', methods=['POST', 'GET'])
#def hello():
 #   count = get_hit_count()
  #  return 'Hello World! I have been seen {} times.\n'.format(count)
def index():

    if request.method == 'POST':
        name = request.json['text']
        redis.rpush('comment', name)
        return jsonify({'text':name})

    if request.method == 'GET':
        return jsonify(redis.lrange('students', 0, -1))

if __name__ =="__main__":
    app.debug = True
    app.run(host="0.0.0.0")
