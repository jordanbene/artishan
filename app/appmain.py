from flask.templating import Flask, render_template
from werkzeug.exceptions import HTTPException
from app import app as app

@app.route('/')
def index():
    print("success")
    #return 'appmain'

    return render_template('index.html', title="Test")

@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors. You wouldn't want to handle these generically.
    if isinstance(e, HTTPException):
        return e

    # now you're handling non-HTTP exceptions only
    return render_template("500_generic.html", e=e), 500