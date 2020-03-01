import ftransc
import os
import subprocess
from pathlib import Path

# fileTypes = ['m4a', 'mp3', 'ogg', 'flac', 'wma', 'mpc', 'wav', 'wv']
# if (str(i).index(fileTypes))

def convertFile(_path, _type):
    print ("Converting files in path: ", _path + ' to ' + _type + " 's.")
    p = Path(_path)
    for i in p.glob('**/*'):
        subprocess.call(['ftransc', '-f', _type, '--directory', str(i)])

convertFile("./The Prodigy", "ogg")


