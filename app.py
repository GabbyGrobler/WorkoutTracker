from flask import Flask

app = Flask(__name__)

@app.route('/') # API Endpoint
def hello_world():
    return '<p>Hello, World!</p>'

@app.route('/test1') # API Endpoint
def hello_world1():
    return '<p>T1</p>'

@app.route('/test2') # API Endpoint
def hello_world2():
    return '<p>T2</p>'

