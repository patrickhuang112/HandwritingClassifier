"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect
from handwriting_classifier import app
import subprocess
import sys
import os
from flask import request


win = False
if sys.platform == "win32":
    win = True

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

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
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Renders the contact page."""
    #user_id = open("handwriting_classifier/userid.txt").read()
    if request.method == "POST":
        count = 1
        if request.form['predictsubmit'] == 'Run':
            ImagePath = request.form['imagepath']
            Model = request.form['model']
            Width = request.form['width']
            Height = request.form['height']
            Flat = request.form['flat']
   
            os.system("python predict.py --image {} --model {} --width {} --height {} --flatten {}".format(ImagePath, Model, Width, Height, str(Flat))) if win else os.system("python3 predict.py --image {} --model {} --width {} --height {} --flatten {}".format(ImagePath, Model, Width, Height, str(Flat))) 
        
        elif request.form['combinersubmit'] == 'Run':
            img1 = request.form['firstpath']
            img2 = request.form['secondpath']
            name = request.form['resultname']
            os.system("python imagecombiner.py --image1 {} --image2 {} --output_name {}".format(img1, img2, name)) if win else os.system("python3 imagecombiner.py --image1 {} --image2 {} --output_name {}".format(img1, img2, name))
    
    return render_template(
        'predict.html',
        title='Predict',
        year=datetime.now().year,
        message='This program will compare two handwriting images and output whether or not they were written by the same person.'
    )
	
@app.route('/reader', methods=['GET', 'POST'])
def reader():
    if request.method == "POST":
        if request.form['readersubmit'] == 'Read':
            ImagePath = request.form['image']
            os.system("python text_from_image.py --toReader {}".format(ImagePath)) if win else os.system("python3 text_from_image.py --toReader {}".format(ImagePath))
        elif request.form['readersubmit'] == 'Find':
            ImagePathF = request.form['path']
            TargetWord = request.form['targetword']
            os.system("python handwriting_word_search.py --image {} --target {}".format(ImagePathF, TargetWord)) if win else os.system("python3 handwriting_word_search.py --image {} --target {}".format(ImagePathF, TargetWord))
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
        print("HEY")
        if sys.platform == 'linux':
            subprocess.call(["python3", "HandwritingGUI.py"])
        elif sys.platform == 'darwin':
            subprocess.call(["python3", "HandwritingGUI.py"])
        else:
            subprocess.call(["python", "HandwritingGUI.py"])
                    
    return redirect('/')


@app.route('/game')
def game():
    return render_template('game.html')


