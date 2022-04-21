from flask import Flask
from flask import render_template
import glidemodel
from werkzeug.exceptions import HTTPException
from app import app as app

@app.route('/')
def main():

    #model = glidemodel.model

    #return render_template('index.html', title="Test")
    return print("success")

@app.errorhandler(500)
def internal_server_error(error):
    # This may pass system errors you do not wish users to see
    return render_template('error.html', error_info=error.args)
