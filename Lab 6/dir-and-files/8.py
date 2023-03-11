import os

path = 'somefile.txt'

if os.path.exists(path) and os.access(path, os.R_OK) and os.access(path, os.W_OK):
    os.remove(path)