import flask
from flask import Flask, render_template, send_file, url_for, jsonify, request, Request, Response, make_response, send_from_directory, flash
from flask import render_template
from logging import WARNING, FileHandler
from app import app
import json
import os, io
@app.route('/', methods=['GET', 'POST'])
def index():
    #app.logger.warning("Routes Accessed Success")
    return render_template('template.html', title="Artishan")

@app.route('/generateimage', methods=['GET', 'POST'])
def generatebutton():
    if flask.request.method == "GET":
       #data = request.get_data()
       app.logger.warning("generate image data: " + data)
       imgname = "name"
       data = jsonify( imgname )

       return jsonify(imgname)
    return render_template('template.html', title="Artishan")

def serve_pil_image(pil_img):
    img_io = io.BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

@app.errorhandler(500)
def internal_server_error(error):
    # This may pass system errors you do not wish users to see
    return render_template('error.html', error_info=error.args)