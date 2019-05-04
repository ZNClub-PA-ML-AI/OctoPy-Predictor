'''Web Runner'''

from flask import Flask, request, redirect, url_for
import context
import util
import json
from util import logit, jsonify
import os


'''define Flask app'''
app = Flask(__name__)
app.config['DEBUG'] = context.DEBUG_MODE


UPLOAD_FORM_HTML_TEMPLATE = """
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form action="" method=post enctype=multipart/form-data>
          <p><input type=file name=file>
             <input type=submit value=Upload>
        </form>
        <p>%s</p>
        """ % "<br>".join(os.listdir(context.UPLOAD_FOLDER,))



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
@logit
def file_upload():
    if request.method == 'POST':                
        file = request.files['file']   
        if file is None or not util.is_allowed_file(file.filename):
            raise ValueError('File Type not supported for Upload. \
            Please upload valid file')                    
        interface.load_data(file = file)        
        return str(interface.get_summary().to_json())
    else:
        return UPLOAD_FORM_HTML_TEMPLATE

@app.route("/debug/inspect", methods=['GET'])
def get_debug_store():
    return json.dumps(util.debug_store)

if __name__ == '__main__':

    context.init_dependencies()
    interface = context.app_context['WebInterface']
    app.run(port=context.HTTP_PORT)
    