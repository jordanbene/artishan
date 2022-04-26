import sys, os

#INTERP = os.path.join(os.environ['HOME'], 'dh_nfjxcr','dh_nfjxcr', 'artishan.io', 'opt', 'python-3.8.2', 'bin', 'python3')

INTERP = os.path.join(os.environ['HOME'], 'artishan.io', 'venv', 'bin', 'python3')
if sys.executable != INTERP:
        os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())


sys.path.append('app')
from app.appmain import app as application
 
x = open(os.path.expanduser('~/artishan.io/log.log'), 'w')
x.write(repr(sys.argv))
x.close()