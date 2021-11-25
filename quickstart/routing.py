from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Index Testing Page"

@app.route('/hello')
def hello():
    return "<center><h1>Hello Testing Page</h1></center>"