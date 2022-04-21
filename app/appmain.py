from logging import WARNING, FileHandler
from flask import Flask, logging
from flask import render_template
import sys, os
import glidemodel
from werkzeug.exceptions import HTTPException
from app import app as app

file_handler = FileHandler('apperrorlog.txt')
file_handler.setLevel(WARNING)
app.logger.addHandler(file_handler)

@app.route('/')
def main():
    app.logger.warning("App Main Accessed Success")
    print("app main accessed")
    return render_template('/static/index.html', title="Artishan")
    #return render_template('index.html', title="Test")

@app.errorhandler(500)
def internal_server_error(error):
    # This may pass system errors you do not wish users to see
    return render_template('error.html', error_info=error.args)
