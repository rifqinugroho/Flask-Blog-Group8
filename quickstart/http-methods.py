from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'WELCOME %s' % name

@app.route('/login', methods = ['POST', 'GET'])
def login():
    print(request.method)
    if request.method == 'POST':
        user = request.form['nama']
        return redirect(url_for('success', name = user))
    else:
        print('Masuk sini')
        user = request.args.get('nama')
        return redirect(url_for('success', name = user))