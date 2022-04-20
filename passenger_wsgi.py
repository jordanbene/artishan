import sys, os
from flask.templating import Flask, render_template


INTERP = os.path.join(os.environ['HOME'], 'artishan.io', 'venv', 'bin', 'python3')
if sys.executable != INTERP:
        os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

from flask import Flask

sys.path.append('app')
from app import appmain as application
 
