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
    user_id = open("handwriting_classifier/userid.txt").read()
    if user_id == '1':
        subprocess.call(["python", r"C:\Users\galbraithja\AppData\Local\Programs\Python\Python37-32\predict.py"])
    elif user_id == '2':
        subprocess.call(["python3", r"/Users/griffinwalraven/programming/NWAPW/handwriting classifier/HandwritingClassifier/predict.py"])
    elif user_id == '3':
        # put loc of predict.py here
        pass
    elif user_id == '4':
        # put loc of predict.py here
        pass
    else:
        print("Invalid user id")

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

