# controller

from flask import Flask, request, redirect, url_for
from flask import jsonify
from flask import Response
import os
from werkzeug import secure_filename
from logging import FileHandler, WARNING

file_handler = FileHandler('octoPy.log')
file_handler.setLevel(WARNING)


app = Flask(__name__)
app.logger.addHandler(file_handler)

''' Server shutdown snippet reference :http://flask.pocoo.org/snippets/67/ '''
@app.route('/shutdown')
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

quotes = {1:'Beautiful is better than ugly.'}

''' Basic Routes'''
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

''' File Upload Snippet reference https://gist.github.com/dAnjou/2874714'''

UPLOAD_FOLDER = r'C:\Users\Augus\dev\Projects\OctoPy-Predictor\octopy_predictor\data'
ALLOWED_EXTENSIONS = set(['txt'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return True
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/data-file", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
    	print(request.headers, request.files)
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
    else:
	    return """
	    <!doctype html>
	    <title>Upload new File</title>
	    <h1>Upload new File</h1>
	    <form action="" method=post enctype=multipart/form-data>
	      <p><input type=file name=file>
	         <input type=submit value=Upload>
	    </form>
	    <p>%s</p>
	    """ % "<br>".join(os.listdir(app.config['UPLOAD_FOLDER'],))


if __name__ == '__main__':
    app.run(port=8080)