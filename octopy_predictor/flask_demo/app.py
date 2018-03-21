# controller

from flask import Flask, request
app = Flask(__name__)

quotes = {1:'Beautiful is better than ugly.'}

@app.route('/')
def hello_world():
    return 'Hello, Welcome to Flask demo!'

@app.route('/quotes/<int:qoute_id>')
def get_quote_by(qoute_id):
	return quotes[qoute_id]

@app.route('/quotes')
def get_all_quotes():
	return str(quotes)

#@app.route('/popular-quote-id/', methods=['GET,POST'])
@app.route('/popular-quote-id/')
def get_popular_quote_id():
	if request.method == 'POST':
		pass
	else:
		return str(1)

# if __name__ == '__main__':
#     app.run(port=8080)