#!/home/dh_nfjxcr/artishan.io/venv/bin/python3

from flask import Flask
from logging import WARNING, FileHandler

app = Flask(__name__, template_folder="templates", static_folder="static")

from . import routes

#error log
file_handler = FileHandler('apperrorlog.txt')
file_handler.setLevel(WARNING)
app.logger.addHandler(file_handler)
#

app.debug = True


