#Handwriting Classifier GUI
#7/15/2019

from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import subprocess
import numpy as np
import PIL
import os

program = "what"

#Runs programs when buttons are clicked
def run_comparison():
    print ("Running Comparison")
    #subprocess.call(["python", "-----.py"])
def run_profiler():
    print ("Running Profiler")
    #subprocess.call(["python", "profiler program"])
def run_reader():
    print ("Running Reader")
    #subprocess.call(["python", "reader program"])
def run():
    ImagePath = b2.get()
    Model = b1.get()
    Width = b4.get()
    Height = b5.get()
    Flat = var1.get()
    os.system('python3 predict.py --image "{}" --model "{}" --width "{}" --height "{}" --flatten "{}"'.format(ImagePath, Model, Label, Width, Height, str(Flat)))
    #subprocess.call(["python", "predict.py"])
    print (ImagePath, Model, Label, Width, Height, Flat)
def preset1():
    print ("PReset")
    b2.delete(0,END)
    b1.delete(0,END)
    b3.delete(0,END)
    b4.delete(0,END)
    b5.delete(0,END)
    #Add text
    b2.insert(0,"ImagePath")
    b1.insert(0,"Model")
    b3.insert(0,"Label")
    b4.insert(0,"Width")
    b5.insert(0,"Flat")
    var1.set(1)
def clear():
    print ("Clear")
    b2.delete(0,END)
    b1.delete(0,END)
    b3.delete(0,END)
    b4.delete(0,END)
    b5.delete(0,END)
    var1.set(0)

#Creates Window
window = tk.Tk()
window.title("Welcome to the Handwriting Classifier")
window.geometry('459x300')
window.configure(background = '#778899')

path1 = "1.jpg"
path2 = "2.jpg"

#Creates Tabs
tabControl = ttk.Notebook(window)
tab0 = ttk.Frame(tabControl)
tabControl.add(tab0, text='Run')
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Programs')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Results")
tabControl.pack(expand=1, fill="both")

#Tab0
tk.Label(tab0, text="Enter Information to Run Prediction", font=("Arial Bold", 10)).grid(column=0,row=0, sticky=W)
tk.Label(tab0, text="Image Path").grid(column=0, row=1, sticky=W)
tk.Label(tab0, text="Model").grid(column=0, row=2,sticky=W)
tk.Label(tab0, text="Path to Label Binarizar").grid(column=0, row=3, sticky=W)
tk.Label(tab0, text="Width").grid(column=0, row=4, sticky=W)
tk.Label(tab0, text="Height").grid(column=0, row=5, sticky=W)
var1 = IntVar()
Checkbutton(tab0, text="Flatten Image", variable=var1).grid(column=1, row=6, sticky=W)

b2 = tk.Entry(tab0)
b2.grid(column=1, row=1)
b1 = tk.Entry(tab0)
b1.grid(column=1, row=2)
b3 = tk.Entry(tab0)
b3.grid(column=1, row=3)
b4 = tk.Entry(tab0)
b4.grid(column=1, row=4)
b5 = tk.Entry(tab0)
b5.grid(column=1, row=5)

btnrun=tk.Button(tab0, text='Run Prediction', command=run, padx=9, pady=2)
btnrun.grid(column=0, row=7, sticky=W)
ex1=tk.Button(tab0, text='Set Example 1', command=preset1,padx=12, pady=2)
ex1.grid(column=0, row=8, sticky=W)
btnc=tk.Button(tab0, text='Clear Entry Boxes', command=clear, padx=3, pady=2)
btnc.grid(column=0, row=9, sticky=W)


#Tab 1
lbl = tk.Label(tab1, text="Handwriting Tools", font=("Arial Bold", 20), padx=25, pady=5)
lbl.grid(columnspan=3, row=0)

btn1 = tk.Button(tab1, text="Run Comparison", padx=30, pady=5, command=run_comparison)
btn1.grid(column=0, row=1)

btn2 = tk.Button(tab1, text=("Run Profiler"), padx=40, pady=5, command=run_profiler)
btn2.grid(column=1, row=1)

btn3 = tk.Button(tab1, text=("Run Reader"), padx=38, pady=5, command=run_reader)
btn3.grid(column=2, row=1)

#Tab 2
title = tk.Label(tab2, text="Example Images", font=("Arial Bold", 20), padx=118, pady=5)
title.grid(columnspan=3, row=0)

#Image 1
img1 = Image.open('photos/1.jpg')
img1 = img1.resize((200, 200), PIL.Image.ANTIALIAS)
img1.save('1.jpg')
img1 = ImageTk.PhotoImage(Image.open(path1))

panel1 = tk.Label(tab2, image = img1)
panel1.grid(column=0, row=1)

#Image 2
img2 = Image.open('photos/2.jpg')
img2 = img2.resize((200, 200), PIL.Image.ANTIALIAS)
img2.save('2.jpg')
img2 = ImageTk.PhotoImage(Image.open(path2))

panel2 = tk.Label(tab2, image = img2)
panel2.grid(column=2, row=1)

window.mainloop()





