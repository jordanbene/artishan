#!/home/dh_nfjxcr/opt/python-3.8.2/bin/python3
import sys, os

INTERP = os.path.join(os.environ['HOME'], 'opt', 'python-3.8.2', 'bin', 'python3')
#INTERP = os.path.join(os.environ['HOME'], 'artishan.io', 'venv', 'bin', 'python3')
if sys.executable != INTERP:
        print("Adding Path")
        os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd(), 'myapp')

#sys.path.append('home/artishan.io/myapp')
sys.path.append(os.path.join(os.environ['HOME'], 'artishan.io', 'myapp'))

sys.path.insert(0,'$HOME/opt/python-3.8.2/bin/python3')
sys.path.insert(0,'$HOME/artishan.io/myapp')
sys.path.insert(0,'$HOME/artishan.io/venv/bin')

from myapp import app as application
 
x = open(os.path.expanduser('~/artishan.io/log.log'), 'w')
x.write(repr(sys.argv))
x.close()