# controller

from flask import Flask
app = Flask(__name__)

global_route = ''
@app.route('/')
def hello_world():
    return 'Hello, World!'