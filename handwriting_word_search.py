#Handwritten Word Search using pytesseract

# Import modules
from PIL import Image, ImageTk
import PIL
import pytesseract
import tkinter as tk
import argparse
import os
import sys

#Argument Parser
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="path to input image")
ap.add_argument("-t", "--target", required=True, help="the word the program will search for")
ap.add_argument("-l", "--launcher", required=False)
args = vars(ap.parse_args())

#Launched by GUI
launched = "0"
try:
    if args["launcher"] == '1':
        launched = '1'
except:
    pass

# Include tesseract executable in your path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Create an image object of PIL library
image = Image.open(args["image"])
target = args["target"]
 
# pass image into pytesseract module
# pytesseract is trained in many languages
image_to_text = pytesseract.image_to_string(image, lang='eng')

# split the text
words = image_to_text.split()
count = 0

    # for each word in the line:
for word in words:
   lowerword = word.casefold()
   #print(lowerword) 
   if lowerword == target:
       count += 1
if count == 1:
    print(target, "occurs 1 time.")
    output = "'" + target + "'" + " occurs 1 time."
else:
    print(target, "occurs", count, "times.")
    output = "'" + target + "'" + " occurs " + str(count) + " times."

#Destroy Window
def close():
   display.destroy()

#Display results in new window
display = tk.Tk()
display.title("Find Word")

result = tk.Label(display, text=output, padx=5, pady=5)
result.grid(column=0, row=0)

#Image 1
image = image.resize((200, 200), PIL.Image.ANTIALIAS)
image.save(args["image"])

copy = image.copy()
copy.save("handwriting_classifier/static/SearchedImage.png")
#write file
file = open("handwriting_classifier/static/SearchResults.txt", "w")
file.write("'" + target + "'" + " occurs " + str(count) + " times.")
file.close()

if launched == '1':
   image = ImageTk.PhotoImage(Image.open(args["image"]))

   panel = tk.Label(display, image = image)
   panel.grid(column=1, row=0)

   display.protocol("WM_DELETE_WINDOW", close)
   display.mainloop()

