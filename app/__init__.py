from flask import Flask

app = Flask(__name__, template_folder="static", static_folder="static")

from app import routes
app.debug = False
