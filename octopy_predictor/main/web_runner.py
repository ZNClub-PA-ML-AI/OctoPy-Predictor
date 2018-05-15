'''Web Runner'''

from flask import Flask, request, redirect, url_for
from context import *
import util
import os
from werkzeug import secure_filename

UPLOAD_FOLDER = r'C:\Users\Augus\dev\Projects\OctoPy-Predictor\octopy_predictor\data'
ALLOWED_EXTENSIONS = set(['txt'])

def allowed_file(filename):
	return True
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

@app.route("/data-file", methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            #filename = secure_filename(file.filename)
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            interface.load_data(file)
            return redirect(url_for('file_upload'))
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

    context = init_dependencies()
    interface = app_context['WebInterface']
    app.run(port=9100)
