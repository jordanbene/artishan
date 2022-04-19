import sys, os

from artishan.app import appmain
INTERP = os.path.join(os.environ['HOME'], 'artishan.io', 'venv', 'bin', 'python3')
if sys.executable != INTERP:
        os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

from flask import Flask
from app import appmain
from app.appmain import application as application

#application = appmain.application

#application = Flask(__name__)


