from flask import Flask, render_template

app = Flask(__name__, template_folder="static", static_folder="static")

from app import routes
