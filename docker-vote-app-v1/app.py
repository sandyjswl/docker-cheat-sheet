from flask import Flask
app = Flask(__name__)

number_of_votes = 0

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/check')
def check():
    return 'Checking In if everything is fine'


@app.route('/vote')
def vote():
    global number_of_votes
    number_of_votes = number_of_votes +1
    return str(number_of_votes)


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')