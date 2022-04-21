from flask import Flask
from flask import render_template
from logging import WARNING, FileHandler
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    #app.logger.warning("Routes Accessed Success")
    return render_template('index.html', title="Artishan")

@app.route('/generate', methods=['GET', 'POST'])
def generatebutton():

@app.errorhandler(500)
def internal_server_error(error):
    # This may pass system errors you do not wish users to see
    return render_template('error.html', error_info=error.args)