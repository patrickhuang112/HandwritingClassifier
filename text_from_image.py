# Import modules
from PIL import Image, ImageTk
import PIL
import pytesseract
import tkinter as tk
import argparse
import os
import sys
 
#argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--toReader", required=True, help="path to image")
ap.add_argument("-l", "--launcher", required=False)
args = vars(ap.parse_args())

#Launched by GUI?
launched = "0"
try:
    if args["launcher"] == '1':
        launched = '1'
except:
    pass

# Include tesseract executable in your path
if win:
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
elif sys.platform == "linux":
    pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
elif sys.platform == "darwin":
    pytesseract.pytesseract.tesseract_cmd = r"" # <-- loc on macos goes here

# Create an image object of PIL library
image = Image.open(args["toReader"])
 
# pass image into pytesseract module
image_to_text = pytesseract.image_to_string(image, lang='eng')

#Close Window
def close():
    display.destroy()

display = tk.Tk()
display.title("Text Reader")

result = tk.Label(display, text=image_to_text, padx=5, pady=5)
result.grid(column=0, row=0)

#Image 1
image = image.resize((200, 200), PIL.Image.ANTIALIAS)
image.save(args["toReader"])
image = ImageTk.PhotoImage(Image.open(args["toReader"]))

panel = tk.Label(display, image = image)
panel.grid(column=1, row=0)

display.protocol("WM_DELETE_WINDOW", close)
display.mainloop()
