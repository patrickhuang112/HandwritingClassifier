#Handwriting Classifier GUI
#7/15/2019

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import subprocess
import numpy as np
import PIL

#Runs programs when buttons are clicked
def run_comparison():
    print ("Running Comparison")
    #subprocess.call(["python", "comparison program"])
def run_profiler():
    print ("Running Profiler")
    #subprocess.call(["python", "profiler program"])
def run_reader():
    print ("Running Reader")
    #subprocess.call(["python", "reader program"])

#Creates Window
window = tk.Tk()
window.title("Welcome to the Handwriting Classifier")
window.geometry('459x300')

path1 = "1.jpg"
path2 = "2.jpg"

#Creates Tabs
tabControl = ttk.Notebook(window)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Programs')
tabControl.pack(expand=1, fill="both")
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Results")

#Tab 1
lbl = tk.Label(tab1, text="Handwriting", font=("Arial Bold", 20), padx=25, pady=5)
lbl.grid(column=1, row=0)

btn1 = tk.Button(tab1, text="Run Comparison", padx=14, pady=5, command=run_comparison)
btn1.grid(column=0, row=1)

btn2 = tk.Button(tab1, text=("Run Profiler"), padx=25, pady=5, command=run_profiler)
btn2.grid(column=1, row=1)

btn3 = tk.Button(tab1, text=("Run Reader"), padx=25, pady=5, command=run_reader)
btn3.grid(column=2, row=1)

#Tab 2
title = tk.Label(tab2, text="Results & Images", font=("Arial Bold", 20), padx=110, pady=5)
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





