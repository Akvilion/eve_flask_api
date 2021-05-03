from flask import Flask, jsonify  # jsonify дозволяє повертати JSON
app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify('Hello World')
