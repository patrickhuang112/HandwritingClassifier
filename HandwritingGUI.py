#Handwriting Classifier GUI
#7/15/2019

import tkinter as tk
from tkinter import ttk

import subprocess

def run_comparison():
    print ("Success")
    subprocess.call(["python", "comparison.py"])

window = tk.Tk()

window.title("Welcome to the Handwriting Classifier")

window.geometry('459x300')

tabControl = ttk.Notebook(window)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Programs')
tabControl.pack(expand=1, fill="both")
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Results")

lbl = tk.Label(tab1, text="Handwriting", font=("Arial Bold", 20), padx=25, pady=5)

lbl.grid(column=1, row=0)

btn1 = tk.Button(tab1, text="Run Comparison", padx=14, pady=5, command=run_comparison)

btn1.grid(column=0, row=1)

btn2 = tk.Button(tab1, text=("Run Profiler"), padx=25, pady=5)

btn2.grid(column=1, row=1)

btn3 = tk.Button(tab1, text=("Run Reader"), padx=25, pady=5)

btn3.grid(column=2, row=1)

window.mainloop()





