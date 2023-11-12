from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World from home"
    
@app.route('/about')    
def about():
    return "Hello, World from about"

if '__name__'== '__main':
	app(debug=True, host='0.0.0.0')