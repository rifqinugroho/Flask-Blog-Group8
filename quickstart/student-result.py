from flask import Flask, app, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("student.html")

@app.route('/result', methods=['POST', 'GET'])
def result():
    error = None
    if request.method == 'POST':
        result = request.form
        return render_template("student-result.html", result = result)