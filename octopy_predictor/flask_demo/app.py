# controller

from flask import Flask, request
from flask import jsonify
from flask import Response

app = Flask(__name__)


''' reference :http://flask.pocoo.org/snippets/67/ '''
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

quotes = {1:'Beautiful is better than ugly.'}

@app.route('/')
def hello_world():
    return 'Hello, Welcome to Flask demo!'

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


@app.route('/quotes/<int:qoute_id>')
def get_quote_by(qoute_id):
	''' typecheck request parameter. Default is string '''
	return quotes[qoute_id]

@app.route('/quotes')
def get_all_quotes():
	return str(quotes)

@app.route('/quotes?responseAs=json')
def get_all_quotes_as_json():
	'''send response as json'''
	js = jsonify(quotes)
	#resp = Response(js, status=200, mimetype='application/json')
	print(js, resp)
	return resp

@app.route('/quotes-by')
def get_all_quotes_by_response_type():
	'''query parameter'''
	resp = quotes
	print(request.args, resp, 'response' in request.args)
	if 'response' in request.args:
		if request.args['response'] == 'json':
			resp = jsonify(quotes)
		elif request.args['response'] == 'text':
			resp = str(quotes)
	print(request.args, type(resp))
	return resp


#@app.route('/popular-quote-id/', methods=['GET,POST'])
@app.route('/popular-quote-id/')
def get_popular_quote_id():
	if request.method == 'POST':
		pass
	else:
		return str(1)

if __name__ == '__main__':
    app.run(port=8080)