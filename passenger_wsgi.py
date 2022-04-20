import sys, os

INTERP = os.path.join(os.environ['HOME'], 'artishan.io', 'venv', 'bin', 'python3')
if sys.executable != INTERP:
        os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

#from flask import Flask

sys.path.append('app')
from app.appmain import app as application
 
if __name__ == '__main__':
    application.run(debug=False)