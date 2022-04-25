
from PIL import Image
import flask
from flask import Flask, render_template, send_file, url_for, jsonify, request, Request, Response, make_response, send_from_directory, flash
from flask import render_template
from logging import WARNING, FileHandler
from app import app
import json
import os, io
import time
import glidemodel

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
IMAGES_FOLDER = os.path.join(APP_ROOT, 'static/images/')


@app.route('/', methods=['GET', 'POST'])
def index():
    #app.logger.warning("Routes Accessed Success")
    return render_template('template.html', title="Artishan")

@app.route('/generateimage', methods=['GET', 'POST'])
def generatebutton():
    if flask.request.method == "POST":
       #data = request.get_data()
       #text = request.get_json(data)
       app.logger.warning("generate image data PRE ")
       if 'value' in request.json:
           value = request.json['value']
           app.logger.warning("generate image data POST: " + value)

       #image_path = 'static/images/default_image.png'

       img = glidemodel.requestimage(value)
       target_path = 'static/images/'
       image_path = saveimage(target_path, img)

       return jsonify(image_path)
    return render_template('template.html', title="Artishan")

@app.errorhandler(500)
def internal_server_error(error):
    # This may pass system errors you do not wish users to see
    return render_template('error.html', error_info=error.args)

def saveimage(target_path, image):

    timestr = time.strftime("%Y%m%d-%H%M%S")
    imgname = "output_image"+timestr+".png"
    image_path = target_path +  imgname
    image.save(image_path)

    return image_path