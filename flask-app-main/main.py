from flask import Flask, render_template
from flask.helpers import url_for
from flask.wrappers import Request
from flask import request
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():
    if Request.method == 'POST' :
        f = open('log.txt', 'a')
        f.write("%s, %s, %s" % (request.form[ 'name' ].request.form[ 'email' ].request.form[ 'message' ]))
        f.close()
    return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/article')
def article():
    return render_template('generic.html')

@app.route('/element')
def element():
    return render_template('elements.html')

app.run()