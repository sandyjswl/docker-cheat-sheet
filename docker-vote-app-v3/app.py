from flask import Flask
import redis
import os

app = Flask(__name__)


r = redis.Redis(
host=os.getenv("REDIS_HOST"),
port=int(os.getenv("REDIS_PORT")))


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/check')
def check():
    return 'Checking In if everything is fine'


@app.route('/vote')
def vote():
    
    votes = r.get("number_of_votes")
    if votes == None:
        votes = 1
        r.set("number_of_votes",votes)
    else:
        votes = int(votes) + 1
        r.set("number_of_votes",votes)
    return str(votes)


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')