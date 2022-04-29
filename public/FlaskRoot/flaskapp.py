#!/home/dh_nfjxcr/artishan.io/venv/bin/python3

from types import NoneType
from typing import DefaultDict
from flask import Flask, render_template, send_file, url_for, jsonify, Request, request, Response, make_response, send_from_directory, flash
#from flask_uploads import UploadSet, configure_uploads, IMAGES
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import flask
import sqlalchemy
import generate
import requests
import json
import base64
import os
import cv2
import shutil


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
IMAGES_FOLDER = os.path.join(APP_ROOT, 'static\\images')
VIDEO_FOLDER = os.path.join(APP_ROOT,'static\\video')
dirname = os.path.dirname(__file__)

app = Flask(__name__)
app.config['IMAGES_FOLDER'] = IMAGES_FOLDER




def allowed_file(filename):
    """
    :param filename: 
    :return: 
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    image_path = IMAGES_FOLDER + "\\" #os.path.join(dirname, r"FlaskRoot\static\images")
    for filename in os.listdir(image_path):
           if filename.startswith('output_image'):  # not to remove other images
                imgname = filename
                return render_template('codextemplate.html', title="Codex", imgname = imgname)
       

    return render_template('codextemplate.html', title="Codex")




@app.route("/about")
def background():
    return render_template('index.html', title="About")

@app.route("/login")
def login():
    return render_template('index.html')

@app.route("/register")
def register():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['upload_folder'], filename))

@app.route('/postimage', methods=['POST', 'GET'])
def postimage():   
    if flask.request.method == "POST":
       #data = request.get_data()
       image_path = IMAGES_FOLDER + "\\" #os.path.join(dirname, r"FlaskRoot\static\images")

       for filename in os.listdir(image_path):
           if filename.startswith('output_image'):  # not to remove other images
                print("Removing Image!  " + filename )
                os.remove(image_path + filename)
       print("POST IMAGE SLIDER VALS  " + str(slider_A) + str(slider_B) + str(slider_C) + str(slider_D) + str(slider_E))

       imgname = generate.generate_art(slider_A, slider_B, slider_C, slider_D, slider_E)
       data = imgname
       print("Generated filename!  " + imgname)


       return jsonify(imgname)



    return render_template('codextemplate.html', title="Error")
       #return send_file(path, mimetype='image/png')  
slider_A = 1
slider_B = 1
slider_C = 1
slider_D = 1
slider_E = 1
slider_F = 1

@app.route("/postslider", methods=["GET", "POST"])
def postSlider():
     if request.method == 'POST':
        data = json.dumps(request.json)
        for key in data:
            value = data[key]
            print("The key and value are ({}) = ({})".format(key, value)) #trying to fugure out how to cycle through data
    

@app.route("/postsliderr", methods=["GET", "POST"])
def postsliderr():
    if request.method == 'POST':
        data = json.dumps(request.json)
        value = 1
        if 'sliderA' in request.json:
            value = request.json['sliderA']
            value = (int(value))
            global slider_A
            slider_A = value
            print("POST SLIDER A Value:  " + str(slider_A))
        if 'sliderB' in request.json:
            value = request.json['sliderB']
            value = (int(value))
            global slider_B
            slider_B = value
            print("POST SLIDER B Value:  " + str(slider_B))
        if 'sliderC' in request.json:
            value = request.json['sliderC']
            value = (int(value))
            global slider_C
            slider_C = value
            print("POST SLIDER C Value:  " + str(slider_C))     
        if 'sliderD' in request.json:
            value = request.json['sliderD']
            value = (int(value))
            global slider_D
            slider_D = value
            print("POST SLIDER D Value:  " + str(slider_D))
        if 'sliderE' in request.json:
            value = request.json['sliderE']
            value = (int(value))
            global slider_E
            slider_E = value
            print("POST SLIDER E Value:  " + str(slider_E))
        if 'sliderF' in request.json:
            value = request.json['sliderF']
            value = (int(value))
            global slider_F
            slider_F = value
            print("POST SLIDER F Value:  " + str(slider_F))

       

        return jsonify(value)
    else:
        
        print("GET SLIDER RESULT!: " + result + " END")
    
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True) 

