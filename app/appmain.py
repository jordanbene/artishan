from flask.templating import Flask, render_template
from app import app as app

@app.route('/')
@app.route('/index')
def index():
    print("success")
    #return 'appmain'

    return render_template('index.html', title="Test")

@app.errorhandler(404)
def pageNotFound(error):
    return "page not found", 404

@app.errorhandler(500)
def special_exception_handler(error):
    return "Database connection failed", 500