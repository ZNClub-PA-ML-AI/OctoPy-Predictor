'''Web Runner'''

from flask import Flask, request
from context import *

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, Welcome to Flask demo!'


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


if __name__ == '__main__':

    context = init_dependencies()
    app.run(port=9100)
