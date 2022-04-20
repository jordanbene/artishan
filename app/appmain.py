from flask.templating import Flask, render_template
from app import app
application = app

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return 'appmain'

    #return render_template('index.html', title="Test")

