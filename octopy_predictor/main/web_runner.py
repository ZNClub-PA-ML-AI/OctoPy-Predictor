'''Web Runner'''

from flask import Flask, request

if __name__ == '__main__':

    context = init_dependencies()

    app = Flask(__name__)
    app.run(port=9001)
