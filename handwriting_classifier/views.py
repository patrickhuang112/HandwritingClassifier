"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, request, flash, redirect
from handwriting_classifier import app
import subprocess
import sys
import os
from werkzeug.utils import secure_filename
import urllib.request
from os import path
import shutil
from PIL import Image

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    
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
        message='These programs take an image and either output the text or find the number of occurances for a specific word.'
    )
@app.route('/compare', methods=['GET', 'POST'])
def predict():
    """Renders the contact page."""
    #user_id = open("handwriting_classifier/userid.txt").read()
    if request.method == "POST":
        if request.form['predictsubmit'] == 'Predict':
            ImagePath = request.form['imagepath']
            Model = request.form['model']
            Width = request.form['width']
            Height = request.form['height']
            Flat = request.form['flat']

            os.system("python predict.py --image {} --model {} --width {} --height {} --flatten {}".format(ImagePath, Model, Width, Height, str(Flat))) if win else os.system("python3 predict.py --image {} --model {} --width {} --height {} --flatten {}".format(ImagePath, Model, Width, Height, str(Flat))) 
         
        elif request.form['predictsubmit'] == 'Combine':
            img1 = request.form['firstpath']
            img2 = request.form['secondpath']
            name = request.form['resultname']
            os.system("python imagecombiner.py --image1 {} --image2 {} --output_name {}".format(img1, img2, name)) if win else os.system("python3 imagecombiner.py --image1 {} --image2 {} --output_name {}".format(img1, img2, name))
       
    return render_template(
        'predict.html',
        title='Compare',
        year=datetime.now().year,
        message='This program will combine then compare two handwriting images and output whether or not they were written by the same person.'
    )

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method =='POST':
        file = request.files['file']
        file2 = request.files['file2']
        if file.filename == '':
            flash('No first file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            extension = filename[filename.index('.'):]
            print(extension)
            file.save(os.path.join(os.path.expanduser('~'),'HandwritingClassifier\\photos','imageOne.png'))
            #img = Image.open(os.path.expanduser('~')+'\\'+'\\HandwritingClassifier\\photos\\imageOne'+extension)
            #img.save(os.path.expanduser('~')+'\\'+'\\HandwritingClassifier\\photos\\imageOne' + ".png")
        if file2.filename == '':
            flash('No second file selected for uploading')
            return redirect(request.url)
        if file2 and allowed_file(file2.filename):
            filename = secure_filename(file2.filename)
            extension = filename[filename.index('.'):]
            print(extension)
            file2.save(os.path.join(os.path.expanduser('~'),'HandwritingClassifier\\photos','imageTwo.png'))
            
            flash('File successfully uploaded')
            #return redirect('/predict')
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)
        print("YEEET")
        img1 = 'photos{}imageOne.png'.format(os.path.sep)
        img2 = 'photos{}imageTwo.png'.format(os.path.sep)
        name = 'combinedImage'
        os.system("python imagecombiner.py --image1 {} --image2 {} --output_name {}".format(img1, img2, name)) if win else os.system("python3 imagecombiner.py --image1 {} --image2 {} --output_name {}".format(img1, img2, name))

        ImagePath = 'handwriting_classifier/static/combinedImage.png'
        Model = 'output/simple_nn2.model'
        Width = '32'
        Height = '32'
        Flat = '1'

        try:
            if request.form['predict'] == '1':
                os.system("python predict.py --image {} --model {} --width {} --height {} --flatten {}".format(ImagePath, Model, Width, Height, str(Flat))) if win else os.system("python3 predict.py --image {} --model {} --width {} --height {} --flatten {}".format(ImagePath, Model, Width, Height, str(Flat))) 
        except:
            pass
         
        return redirect('/compare')

    
@app.route('/uploadreader', methods=['GET', 'POST'])
def text_reader():
    if request.method =='POST':
        file = request.files['text']
        if file.filename == '':
            flash('No first file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            extension = filename[filename.index('.'):]
            print(extension)
            file.save(os.path.join(os.path.expanduser('~'),'HandwritingClassifier\\photos','text_read.png'))
            #img = Image.open(os.path.expanduser('~')+'\\'+'\\HandwritingClassifier\\photos\\imageOne'+extension)
            #img.save(os.path.expanduser('~')+'\\'+'\\HandwritingClassifier\\photos\\imageOne' + ".png")
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)
        ImagePath = 'photos/text_read.png'

        os.system("python text_from_image.py --toReader {}".format(ImagePath)) if win else os.system("python3 text_from_image.py --toReader {}".format(ImagePath)) 
   

        return redirect('/reader')
    
@app.route('/uploadfinder', methods=['GET', 'POST'])
def text_finder():
    if request.method =='POST':
        file = request.files['text']
        if file.filename == '':
            flash('No first file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            extension = filename[filename.index('.'):]
            print(extension)
            file.save(os.path.join(os.path.expanduser('~'),'HandwritingClassifier\\photos','text_find.png'))
            #img = Image.open(os.path.expanduser('~')+'\\'+'\\HandwritingClassifier\\photos\\imageOne'+extension)
            #img.save(os.path.expanduser('~')+'\\'+'\\HandwritingClassifier\\photos\\imageOne' + ".png")
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)
        ImagePathF = 'photos{}text_find.png'.format(os.path.sep)
        TargetWord = request.form['targetword']
        os.system("python handwriting_word_search.py --image {} --target {}".format(ImagePathF, TargetWord)) if win else os.system("python3 handwriting_word_search.py --image {} --target {}".format(ImagePathF, TargetWord)) 

        return redirect('/reader')

	
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
        title='Read',
        year=datetime.now().year,
        message='These programs take an image and either output the text or find the number of occurances for a specific word.'
    )

	
@app.route('/run', methods=['GET', 'POST'])
def run():
    if request.method == "POST":
        if request.form['gui_button'] == "Run here >>":
            print("yeet")
            if sys.platform == 'linux':
                subprocess.call(["python3", "HandwritingGUI.py"])
            elif sys.platform == 'darwin':
                subprocess.call(["python3", "HandwritingGUI.py"])
            else:
                subprocess.call(["python", "HandwritingGUI.py"])        
    return render_template('home.html')           




@app.route('/game')
def game():
    return render_template('game.html')


