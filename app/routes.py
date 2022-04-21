from flask import Flask
from flask import render_template
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    #print("routes accessed")
    #return render_template('index.html', title="Test Title From Routes")
    return print("routes accessed")

