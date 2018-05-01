'''Web Runner'''

from flask import Flask, request
from context import *
import util

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, Welcome to Flask demo!'

@app.route('/shutdown', methods=['POST'])
def shutdown():
    util.shutdown_server()
    return 'Server shutting down...'


if __name__ == '__main__':

    context = init_dependencies()
    app.run(port=9100)
