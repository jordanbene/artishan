from flask.templating import Flask, render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html', title="Test")
