'''Web Runner'''

from flask import Flask, request
from context import *
import util

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
   return 'Hello, Welcome to Octo-Py'

@app.route('/shutdown', methods=['POST'])
def shutdown():
    util.shutdown_server()
    return 'Server shutting down...'

@app.route('/<string:username>', methods=['GET'])
def greet(username):
   return interface.greet(username)

if __name__ == '__main__':

    context = init_dependencies()
    interface = app_context['WebInterface']
    app.run(port=9100)
