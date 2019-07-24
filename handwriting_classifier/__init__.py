"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.config['TESTING']= True
app.config['TEMPLATES_AUTO_RELOAD'] = True

import handwriting_classifier.views



