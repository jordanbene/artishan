from flask import Flask
from logging import WARNING, FileHandler

app = Flask(__name__, template_folder="templates", static_folder="static")

from app import routes

#error log
file_handler = FileHandler('apperrorlog.txt')
file_handler.setLevel(WARNING)
app.logger.addHandler(file_handler)
#

app.debug = False


