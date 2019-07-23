"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from handwriting_classifier import app
import subprocess
import sys
import os
from flask import request

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'home.html',
        title='Home',
        year=datetime.now().year,
    )

@app.route('/about')
def about():
    """Renders the contact page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Displays results of the calculation.'
    )
@app.route('/predict')
def predict():
    """Renders the contact page."""
    subprocess.call(["python3", "../../predict.py"])

    return render_template(
        'predict.html',
        title='Run Predict.py',
        year=datetime.now().year,
        message='My attempt at running the neural network algorithm. Yeet!'
    )
	
@app.route('/reader')
def reader():
    """Renders the contact page."""
    return render_template(
        'reader.html',
        title='Reader',
        year=datetime.now().year,
        message='Displays results of the calculation.'
    )
	
@app.route('/run', methods=['GET', 'POST'])
def run():
    if request.method == "POST":
        if request.form['submit'] == 'run':
            subprocess.call(["python", "\..\..\HandwritingGUI.py"])
        return render_template('predict.html')
    else:
        return render_template('reader.html')

