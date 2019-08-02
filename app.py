"""
This script runs the handwriting_classifier application using a development server.
"""

from os import environ, system
from handwriting_classifier import app
import argparse
import sys


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--id", required=False,
	help="User id for ease of use", default='1')
args = vars(ap.parse_args())


if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 8000
    if sys.platform == "darwin":
        system("rm handwriting_classifier/userid.txt")
    elif sys.platform == "win32":
        system("del handwriting_classifier/userid.txt")
    else:
        print(sys.platform)
    
    app.run(HOST, PORT, threaded=True)

