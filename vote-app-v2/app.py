from flask import Flask,request, jsonify
import os
app = Flask(__name__)

candidates = {}

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/check')
def check():
    return 'Checking In if everything is fine'


@app.route('/vote/<candidate>')
def vote(candidate):
    if candidate.upper() in candidates:
        candidates[candidate.upper()] += 1
        return jsonify(success=True)
    return jsonify(success=False)

@app.route('/register', methods = ['POST'])
def register():
    try:
        data =request.get_json()
        candidates[data['name'].upper()] = 0
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/candidates', methods = ['GET'])
def get_candidates():
    return candidates

@app.route('/winner', methods = ['GET'])
def get_winner():
    try:
        return str(list({k: v for k, v in sorted(candidates.items(), key=lambda item: item[1])}.keys())[0])+"\n"
    except:
        return jsonify(success=False)

@app.route('/version', methods = ['GET'])
def get_version():
    version = os.getenv("VERSION")
    if version is not None:
        return version
    return jsonify(success=False)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')