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
@app.route('/programs')
def programs():
    """Renders the home page."""
    return render_template(
        'programs.html',
        title='Programs',
        year=datetime.now().year,
    )

@app.route('/results')
def results():
    """Renders the contact page."""
    return render_template(
        'results.html',
        title='Results',
        year=datetime.now().year,
        message='Displays results of the calculation.'
    )
@app.route('/runpredict')
def runpredict():
    """Renders the contact page."""
    subprocess.call(["python", r"../../predict.py"])

    return render_template(
        'runpredict.html',
        title='Run Predict.py',
        year=datetime.now().year,
        message='My attempt at running the neural network algorithm. Yeet!'
    )
	
@app.route('/run', methods=['GET', 'POST'])
def run():
    if request.method == "POST":
        if request.form['submit'] == 'run':
            subprocess.call(["python", "../../HandwritingGUI.py"])
        return render_template('runpredict.html')
    else:
        return render_template('results.html')

