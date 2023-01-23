#!/opt/python

import os

#args = ("test", "abc")
#os.execvp("test.sh", args)

env = {"PATH":"/home/mark/www/twiki/docs/media", "XYZ":"BlaBla"}
args = ("test", "abc")
os.execvpe("test.sh", args, env)
