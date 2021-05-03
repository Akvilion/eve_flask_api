from flask import Flask, jsonify  # jsonify дозволяє повертати JSON
app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({'message': 'Hello World'})


@app.route('/login')
def login():
    return jsonify({'login': 1})