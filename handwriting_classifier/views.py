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
import cv2


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

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
        message='These programs take an image and either output the text or find the number of occurances for a specific word. Click for more information'
    )
@app.route('/compare', methods=['GET', 'POST'])
def predict():
    """Renders the contact page."""
    #user_id = open("handwriting_classifier/userid.txt").read()
    if request.method == "POST":
        """if request.form['predictsubmit'] == 'Predict':
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
"""
    with open('handwriting_classifier/static/truefalse.txt', 'r') as g:
        truefalse = g.read()
    networks = ['Select Neural Network:', 'Simple', 'Convolutional', 'Siamese']
    return render_template(
        'predict.html',
        truefalse=truefalse,
        networks=networks,
        title='Compare',
        year=datetime.now().year,
        message='This program will combine then compare two handwriting images and output whether or not they were written by the same person. Click for more instructions'
    )

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method =='POST':
        file = request.files['file']
        file2 = request.files['file2']
        if file.filename == '':
            
            return 'No first file selected for uploading'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            global extension1
            extension1 = filename[filename.index('.'):]
            #file.save(os.path.join(os.path.expanduser('~'),'HandwritingClassifier/photos','imageOne.png'))
            file.save('photos/imageOne' + extension1)
            #img = Image.open(os.path.expanduser('~')+'\\'+'\\HandwritingClassifier\\photos\\imageOne'+extension)
            #img.save(os.path.expanduser('~')+'\\'+'\\HandwritingClassifier\\photos\\imageOne' + ".png")
        if file2.filename == '':
            return 'No second file selected for uploading'
        if file2 and allowed_file(file2.filename):
            filename = secure_filename(file2.filename)
            global extension2
            extension2 = filename[filename.index('.'):]
            #file2.save(os.path.join(os.path.expanduser('~'),'HandwritingClassifier/photos','imageTwo.png'))
            file2.save('photos/imageTwo' + extension2)
            #return redirect('/predict')
        else:
            return 'Allowed file types are png, jpg, jpeg, gif'
        img1 = 'photos/imageOne' + extension1
        img2 = 'photos/imageTwo' + extension2
        name = 'combinedImage'
        os.system("python imagecombiner.py --image1 {} --image2 {} --output_name {}".format(img1, img2, name)) if win else os.system("python3 imagecombiner.py --image1 {} --image2 {} --output_name {}".format(img1, img2, name))

        try:
            if request.form['predict'] == '1':
                if request.form['network'] == "Select Neural Network:":
                    print ("You fail")
                elif request.form['network'] == "Simple":
                    print ("Simple")
                    ImagePath = 'handwriting_classifier/static/combinedImage.png'
                    Model = 'output/simple_nn2.model'
                    Width = '32'
                    Height = '32'
                    Flat = '1'
                    os.system("python predict.py --image {} --model {} --width {} --height {} --flatten {}".format(ImagePath, Model, Width, Height, str(Flat))) if win else os.system("python3 predict.py --image {} --model {} --width {} --height {} --flatten {}".format(ImagePath, Model, Width, Height, str(Flat))) 
                elif request.form['network'] == "Convolutional":
                    print ("Convolutional")
                    ImagePath = 'handwriting_classifier/static/combinedImage.png'
                    Model = 'output/finalconvolutional.model'
                    Width = '32'
                    Height = '32'
                    Flat = '0'
                    os.system("python predict.py --image {} --model {} --width {} --height {} --flatten {}".format(ImagePath, Model, Width, Height, str(Flat))) if win else os.system("python3 predict.py --image {} --model {} --width {} --height {} --flatten {}".format(ImagePath, Model, Width, Height, str(Flat))) 
                else:
                    print ("Siamese")
                    Image1 = 'photos/imageOne' + extension1
                    Image2 = 'photos/imageTwo' + extension2
                    Model = 'siamese stuff/m1.model'
                    Width = '256'
                    Height = '64'
                    os.system("python predict2.py -i1 {} -i2 {} -m {} -w {} -h {}".format(Image1, Image2, Model, Width, Height)) if win else os.system("python3 predict2.py -i1 {} -i2 {} -m {} -w {} -h {}".format(Image1, Image2, Model, Width, Height)) 
                    image = cv2.imread("handwriting_classifier/static/combinedImage.png")
                    cv2.imwrite("handwriting_classifier/static/outputImage.png", image)
        except:
            pass
         
        return redirect('/compare')

    
@app.route('/uploadreader', methods=['GET', 'POST'])
def text_reader():
    if request.method =='POST':
        file = request.files['text']
        if file.filename == '':
            return "No file selected for uploading"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            global extension_reader
            extension_reader = filename[filename.index('.'):]
            #file.save(os.path.join(os.path.expanduser('~'),'HandwritingClassifier/photos','text_read.png'))
            file.save('photos/text_read' + extension_reader)
            #img = Image.open(os.path.expanduser('~')+'\\'+'\\HandwritingClassifier\\photos\\imageOne'+extension)
            #img.save(os.path.expanduser('~')+'\\'+'\\HandwritingClassifier\\photos\\imageOne' + ".png")
        else:
            return 'Allowed file types are png, jpg, jpeg, gif'
        ImagePath = 'photos/text_read' + extension_reader

        os.system("python text_from_image.py --toReader {}".format(ImagePath)) if win else os.system("python3 text_from_image.py --toReader {}".format(ImagePath)) 
   

        return redirect('/reader')
    
@app.route('/uploadfinder', methods=['GET', 'POST'])
def text_finder():
    if request.method =='POST':
        file = request.files['text']
        if file.filename == '':
            return "No file selected for uploading"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            global extension_finder
            extension_finder = filename[filename.index('.'):]
            print(extension_finder)
            #file.save(os.path.join(os.path.expanduser('~'),'HandwritingClassifier/photos','text_find.png'))
            file.save('photos/text_find' + extension_finder)
            #img = Image.open(os.path.expanduser('~')+'\\'+'\\HandwritingClassifier\\photos\\imageOne'+extension)
            #img.save(os.path.expanduser('~')+'\\'+'\\HandwritingClassifier\\photos\\imageOne' + ".png")
        else:
            return 'Allowed file types are png, jpg, jpeg, gif'
        ImagePathF = 'photos/text_find' + extension_finder
        TargetWord = request.form['targetword']
        os.system("python handwriting_word_search.py --image {} --target {}".format(ImagePathF, TargetWord)) if win else os.system("python3 handwriting_word_search.py --image {} --target {}".format(ImagePathF, TargetWord)) 

        return redirect('/reader')

	
@app.route('/reader', methods=['GET', 'POST'])
def reader():
    """if request.method == "POST":
        if request.form['readersubmit'] == 'Read':
            ImagePath = request.form['image']

            os.system("python text_from_image.py --toReader {}".format(ImagePath)) if win else os.system("python3 text_from_image.py --toReader {}".format(ImagePath)) 
   
        elif request.form['readersubmit'] == 'Find':
            ImagePathF = request.form['path']
            TargetWord = request.form['targetword']
            os.system("python handwriting_word_search.py --image {} --target {}".format(ImagePathF, TargetWord)) if win else os.system("python3 handwriting_word_search.py --image {} --target {}".format(ImagePathF, TargetWord)) 
"""
    #with open(os.path.expanduser('~')+"/"+"HandwritingClassifier/handwriting_classifier/static/ReadResults.txt", "r") as f:
    with open('handwriting_classifier/static/ReadResults.txt', 'r') as f:
        content = f.read()
    #with open(os.path.expanduser('~')+"/"+"HandwritingClassifier/handwriting_classifier/static/SearchResults.txt", "r") as g:
    with open('handwriting_classifier/static/SearchResults.txt', 'r') as g:
        content2 = g.read()
    """Renders the contact page."""
    return render_template(
        'reader.html',
        content=content,
        content2=content2,
        title='Read',
        year=datetime.now().year,
        message='These programs take an image and either output the text or find the number of occurances for a specific word.'
    )

	
@app.route('/run', methods=['GET', 'POST'])
def run():
    if request.method == "POST":
        if request.form['gui_button'] == "Run here >>":
            if sys.platform == 'linux':
                subprocess.call(["python3", "HandwritingGUI.py"])
            elif sys.platform == 'darwin':
                subprocess.call(["python3", "HandwritingGUI.py"])
            else:
                subprocess.call(["python", "HandwritingGUI.py"])        
    return render_template('home.html')           

'''@app.route('/dropdown', methods=['GET'])
def dropdown():
    networks = ['Select Neural Network:', 'Simple', 'Convolutional', 'Siamese']
    return render_template('predict.html', networks=networks)'''


@app.route('/game')
def game():
    return render_template('game.html')


