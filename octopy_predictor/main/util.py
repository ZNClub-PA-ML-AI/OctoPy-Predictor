''' utility methods '''
import logging
import json
import pandas as pd
from flask import request
from functools import wraps

logging.basicConfig(filename='{}.log'.format('app'), level=logging.INFO)
log = logging
debug_store = {}

''' reference :http://flask.pocoo.org/snippets/67/ '''
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

''' reference :https://github.com/CoreyMSchafer/code_snippets/blob/master/Decorators/decorators.py '''
def logit(orig_func):
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        log.info(
            '{}.{} invoked with args: {}, and kwargs: {}'
        .format(orig_func.__module__, orig_func.__name__, args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper

''' '''
def inspect(orig_func):
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        for i in args:
            debug_store[orig_func.__name__] = i
        log.info('storing in debug_store ({},{})'
        .format(orig_func.__name__, args)) 
        return orig_func(*args, **kwargs)
    return wrapper

def jsonify(orig_func):
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        json_result = None
        log.info('jsonify result of {} with args as {})'
        .format(orig_func.__name__, args)) 
        result = orig_func(*args, **kwargs)
        if isinstance(result, pd.core.frame.DataFrame):
            json_result = result.to_json(orient='columns')
        else:
            json_result = json.dumps(result)
        debug_store[orig_func.__module__+orig_func.__name__] = json_result
        return json_result
    return wrapper