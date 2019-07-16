#Handwriting Classifier GUI
#7/15/2019

from tkinter import*

def run_comparison():
    print ("Success")

window = Tk()

window.title("Welcome to the Handwriting Classifier")

window.geometry('459x300')

lbl = Label(window, text="Handwriting", font=("Arial Bold", 20), padx=25, pady=5)

lbl.grid(column=1, row=0)

btn1 = Button(window, text="Run Comparison", padx=14, pady=5, command=run_comparison)

btn1.grid(column=0, row=1)

btn2 = Button(window, text=("Run Profiler"), padx=25, pady=5)

btn2.grid(column=1, row=1)

btn3 = Button(window, text=("Run Reader"), padx=25, pady=5)

btn3.grid(column=2, row=1)

window.mainloop()


