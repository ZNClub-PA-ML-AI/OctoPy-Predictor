''' utility methods '''
from flask import request

''' reference :http://flask.pocoo.org/snippets/67/ '''
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


