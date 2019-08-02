"""
The flask application package.
"""

from flask import Flask
import os


UPLOAD_FOLDER = 'predictPhotos{}'.format(os.path.sep)

app = Flask(__name__)
app.secret_key = "secret key"
app.config['TESTING']= True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


import handwriting_classifier.views

