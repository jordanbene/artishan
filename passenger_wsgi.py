#!/home/dh_nfjxcr/artishan.io/venv/bin/python3
import sys, os

INTERP = os.path.join(os.environ['HOME'], 'artishan.io', 'venv', 'bin', 'python3')
if sys.executable != INTERP:
        os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

#sys.path.append('home/artishan.io/myapp')
sys.path.append(os.path.join(os.environ['HOME'], 'artishan.io', 'myapp'))

#sys.path.append('myapp')
from myapp import app as application
 
x = open(os.path.expanduser('~/artishan.io/log.log'), 'w')
x.write(repr(sys.argv))
x.close()