from flask.templating import Flask, render_template
from app import app as app

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    print("success")
    return 'appmain'

    #return render_template('index.html', title="Test")

