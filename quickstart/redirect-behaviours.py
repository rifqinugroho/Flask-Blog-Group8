from flask import Flask

app = Flask(__name__)

@app.route('/projects/')
def projects():
    return 'Project Page'
    
@app.route('/about')
def about():
    return 'About Page'
