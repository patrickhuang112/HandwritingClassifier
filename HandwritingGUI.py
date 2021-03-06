#Handwriting Classifier GUI
#7/15/2019

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
import subprocess
import numpy as np
import PIL
import os
import sys

imgpath1 = ''
imgpath2 = ''
win = False
if sys.platform == 'win32':
    win = True

#Runs programs when buttons are clicked
def run_comparison():
    ImageWF = "TestImage.jpg"
    Target = "my"
    launch = '1'
    os.system("python handwriting_word_search.py --image {} --target {} --launcher {}".format(ImageWF, Target, launch)) if win else os.system("python3 handwriting_word_search.py --image {} --target {} --launcher {}".format(ImageWF, Target, launch))
def run_profiler():
    path = "TestImage.jpg"
    launch = '1'
    os.system("python text_from_image.py --toReader {} --launcher {}".format(path, launch)) if win else os.system("python3 text_from_image.py --toReader {} --launcher {}".format(path, launch))
def run_reader():
    path = r1.get()
    launch = '1'
    os.system("python text_from_image.py --toReader {} --launcher {}".format(path, launch)) if win else os.system("python3 text_from_image.py --toReader {} --launcher {}".format(path, launch)) 
def readEX():
    r1.delete(0,END)
    r1.insert(0,"TestImage.jpg")

# def defaultPredict():
#     ImagePath = "photos/falseEX.png"
#     Model = "output/simple_nn2.model"
#     Width = "32"
#     Height = "32"
#     Flat = "1"
#     launch = '1'
#     os.system("python predict.py --image {} --model {} --width {} --height {} --flatten {} --launcher {}".format(ImagePath, Model, Width, Height, str(Flat), launch)) if win else os.system("python3 predict.py --image {} --model {} --width {} --height {} --flatten {} --launcher {}".format(ImagePath, Model, Width, Height, str(Flat), launch)) 

def runWF():
    ImageWF = e1.get()
    Target = e2.get()
    launch = '1'
    os.system("python handwriting_word_search.py --image {} --target {} --launcher {}".format(ImageWF, Target, launch)) if win else os.system("python3 handwriting_word_search.py --image {} --target {} --launcher {}".format(ImageWF, Target, launch))
# def preset(num):
#     #Delete text in boxes
#     b2.delete(0,END)
#     b1.delete(0,END)
#     b4.delete(0,END)
#     b5.delete(0,END)
#     #Add text
#     b2.insert(0,"photos/"+num+".png") 
#     b1.insert(0,"output/simple_nn2.model")
#     b4.insert(0,"32")
#     b5.insert(0,"32")
#     var1.set(1)
def findEX():
    e1.delete(0,END)
    e2.delete(0,END)
    e1.insert(0,"TestImage.jpg")
    e2.insert(0,"the")
def clearWF():
    e1.delete(0,END)
    e2.delete(0,END)
def clear():
    b2.delete(0,END)
    b1.delete(0,END)
    b4.delete(0,END)
    b5.delete(0,END)
    var1.set(0)
def clearR():
    r1.delete(0,END)
def clearC():
    c1.delete(0,END)
    c2.delete(0,END)
    c3.delete(0,END)
def combine(outputname):
    output = outputname
    path1 = imgpath1
    print(path1)
    path2 = imgpath2
    print(path2)
    launch = '1'
    os.system("python imagecombiner.py --image1 {} --image2 {} --output_name {} --launcher {}".format(path1, path2, output, launch)) if win else os.system("python3 imagecombiner.py --image1 {} --image2 {} --output_name {} --launcher {}".format(path1, path2, output, launch))
    

def run():
    combine('testcombined')
    Model = "output/simple_nn2.model"
    Width = "32"
    Height = "32"
    Flat = "1" 
    launch = '1'
    os.system("python predict.py --image {} --model {} --width {} --height {} --flatten {} --launcher {}".format('photos/testcombined.jpg', Model, Width, Height, str(Flat), launch)) if win else os.system("python3 predict.py --image {} --model {} --width {} --height {} --flatten {} --launcher {}".format('/combined.jpg', Model, Width, Height, str(Flat), launch)) 
    

def close():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        window.destroy() 

def openFile(btnnum):
    file = filedialog.askopenfile(parent = tab0, mode = 'rb', title = 'Choose a file')
    if file != None:
        data = file.read()
        file.close()
        if btnnum == 1:
            global imgpath1
            imgpath1 = file.name
            print(imgpath1)
        elif btnnum == 2:
            global imgpath2
            imgpath2 = file.name
            print(imgpath2)

        if sys.platform == 'win32':
            print('Loaded {}'.format(file.name.split('/')[-1]))
        else:
            print('Loaded {}'.format(file.name))

        



#Creates Window
window = tk.Tk()
window.title("Welcome to the Handwriting Classifier")
window.geometry('459x300')

#path1 = "1.jpgs"
#path2 = "2.jpg"

#Creates Tabs
tabControl = ttk.Notebook(window)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Home')
#tab2 = ttk.Frame(tabControl)
#tabControl.add(tab2, text="Results")
tab0 = ttk.Frame(tabControl)
tabControl.add(tab0, text='Predict')
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text="Word Find")
tab4 = ttk.Frame(tabControl)
tabControl.add(tab4, text='Reader')
tab5 = ttk.Frame(tabControl)
tabControl.add(tab5, text='Combine Images')
tabControl.pack(expand=1, fill="both")

btnimg1 = tk.Button(tab0, text = 'Select first image', command = lambda: openFile(1), padx=10, pady=5)
btnimg1.grid(column = 0, row = 1, sticky = W, padx=10, pady=5) 


btnimg2 = tk.Button(tab0, text = 'Select second image', command = lambda: openFile(2), padx=10, pady=5)
btnimg2.grid(column = 0, row = 2, sticky = W, padx=10, pady=5)


btnrun=tk.Button(tab0, text='Run Prediction', command=run, padx=10, pady=5)
btnrun.grid(column=0, row=3, sticky=W, padx=10, pady=5)


#Tab0 (Predict Tab)

# tk.Label(tab0, text="Enter Information to Run Prediction", font=("Arial Bold", 10)).grid(column=0,row=0, sticky=W)
# tk.Label(tab0, text="Image Path").grid(column=0, row=1, sticky=W)
# tk.Label(tab0, text="Model").grid(column=0, row=2,sticky=W)
# tk.Label(tab0, text="Width").grid(column=0, row=4, sticky=W)
# tk.Label(tab0, text="Height").grid(column=0, row=5, sticky=W)
# var1 = IntVar()
# Checkbutton(tab0, text="Flatten Image (for simple neural network models)", variable=var1).grid(column=0, row=6, sticky=W)

# b2 = tk.Entry(tab0)
# b2.grid(column=1, row=1)
# b1 = tk.Entry(tab0)
# b1.grid(column=1, row=2)
# b4 = tk.Entry(tab0)
# b4.grid(column=1, row=4)
# b5 = tk.Entry(tab0)
# b5.grid(column=1, row=5)



# ex1=tk.Button(tab0, text='Set Example 1', command=lambda:preset("trueEX"),padx=12, pady=2)
# ex1.grid(column=0, row=8, sticky=W)
# ex2=tk.Button(tab0, text='Set Example 2', command=lambda:preset("falseEX"),padx=12, pady=2)
# ex2.grid(column=0, row=9, sticky=W)


# btnc=tk.Button(tab0, text='Clear Entry Boxes', command=clear, padx=3, pady=2)
# btnc.grid(column=0, row=10, sticky=W)


#Tab 1

image = Image.open('logo.png')
image = image.resize((400, 250), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)

logo = tk.Label(tab1, image = img)
logo.pack()


# lbl = tk.Label(tab1, text="Handwriting Tools", font=("Arial Bold", 20), padx=25, pady=5)
# lbl.grid(columnspan=3, row=0)

# btn1 = tk.Button(tab1, text="Run Find Word", padx=35, pady=5, command=run_comparison)
# btn1.grid(column=0, row=1)

# btn2 = tk.Button(tab1, text=("Run Reader"), padx=40, pady=5, command=run_profiler)
# btn2.grid(column=1, row=1)

# btn = tk.Button(tab1, text="Run Predict", padx=38, pady=5, command=defaultPredict)
# btn.grid(column=2, row=1)

#Tab 2
"""title = tk.Label(tab2, text="Example Images", font=("Arial Bold", 20), padx=118, pady=5)
title.grid(columnspan=3, row=0)

Image 1
img1 = Image.open('photos/1.jpg')
img1 = img1.resize((200, 200), PIL.Image.ANTIALIAS)
img1.save('1.jpg')
img1 = ImageTk.PhotoImage(Image.open(path1))

panel1 = tk.Label(tab2, image = img1)
panel1.grid(column=0, row=1)

Image 2
img2 = Image.open('photos/2.jpg')
img2 = img2.resize((200, 200), PIL.Image.ANTIALIAS)
img2.save('2.jpg')
img2 = ImageTk.PhotoImage(Image.open(path2))

panel2 = tk.Label(tab2, image = img2)
panel2.grid(column=2, row=1)"""

#Tab3
tk.Label(tab3, text="Enter Information to Run Word Finder", font=("Arial Bold", 10)).grid(column=0,row=0, sticky=W)
tk.Label(tab3, text="Image Path").grid(column=0, row=1, sticky=W)
tk.Label(tab3, text="Target Word").grid(column=0, row=2, sticky=W)

e1 = tk.Entry(tab3)
e1.grid(column=1, row=1)
e2 = tk.Entry(tab3)
e2.grid(column=1, row=2)


btnrun=tk.Button(tab3, text='Run Word Finder', command=runWF, padx=3, pady=2)
btnrun.grid(column=0, row=3, sticky=W)
ex1=tk.Button(tab3, text=' Set  Example', command=findEX,padx=13, pady=2)
ex1.grid(column=0, row=4, sticky=W)
btnc=tk.Button(tab3, text=' Clear Boxes', command=clearWF, padx=16, pady=2)
btnc.grid(column=0, row=5, sticky=W)

#Tab4
tk.Label(tab4, text="Enter Information to Run Reader", font=("Arial Bold", 10)).grid(column=0,row=0, sticky=W)
btn3 = tk.Button(tab4, text=("Run Reader"), padx=10, pady=2, command=run_reader)
btn3.grid(column=0, row=3, sticky=W)
clearbtn = tk.Button(tab4, text="Clear Boxes", padx=10, pady=2, command=clearR)
clearbtn.grid(column=0, row=5, sticky=W)
exbtn = tk.Button(tab4, text=" Set Example", padx=7, pady=2, command=readEX)
exbtn.grid(column=0, row=4, sticky=W)

tk.Label(tab4, text="Image Path").grid(column=0, row=1, sticky=W)

r1 = tk.Entry(tab4)
r1.grid(column=1, row=1)

#Tab5
tk.Label(tab5, text='Enter Image Paths to Run Combiner', font=('Arial Bold', 10)).grid(column=0, row=0, sticky=W)
runbtn = tk.Button(tab5, text='Combine Images', padx=3, pady=2, command=combine)
runbtn.grid(column=0, row=4, sticky=W)
clrbtn = tk.Button(tab5, text='Clear Boxes', padx=18, pady=2, command=clearC)
clrbtn.grid(column=0, row=5, sticky=W)

tk.Label(tab5, text="First Image Path").grid(column=0, row=1, sticky=W)
tk.Label(tab5, text="Second Image Path").grid(column=0, row=2, sticky=W)
tk.Label(tab5, text="Result Name").grid(column=0, row=3, sticky=W)

c1 = tk.Entry(tab5)
c1.grid(column=1, row=1)
c2 = tk.Entry(tab5)
c2.grid(column=1, row=2)
c3 = tk.Entry(tab5)
c3.grid(column=1, row=3)
c3.insert(0,"photos/finalimage")

window.protocol("WM_DELETE_WINDOW", close)
window.mainloop()





