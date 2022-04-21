from flask import Flask
from flask import render_template
import glidemodel
from werkzeug.exceptions import HTTPException
from app import app as app

@app.route('/')
def index():

    print("app main accessed")
    return render_template('/static/index.html', title="Artishan")
    #return render_template('index.html', title="Test")

@app.errorhandler(500)
def internal_server_error(error):
    # This may pass system errors you do not wish users to see
    return render_template('error.html', error_info=error.args)
