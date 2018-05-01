'''Web Runner'''

from flask import Flask, request
from context import *

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, Welcome to Flask demo!'


if __name__ == '__main__':

    context = init_dependencies()
    app.run(port=9100)
