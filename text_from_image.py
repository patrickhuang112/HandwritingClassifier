<<<<<<< HEAD
# Import modules
from PIL import Image
import pytesseract
 
# Include tesseract executable in your path
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\galbraithja\AppData\Local\Tesseract-OCR\tesseract.exe"
 
# Create an image object of PIL library
image = Image.open('1.jpg')
 
# pass image into pytesseract module
# pytesseract is trained in many languages
image_to_text = pytesseract.image_to_string(image, lang='eng')
 
# Print the text
print(image_to_text)
=======
# Import modules
from PIL import Image, ImageTk
import PIL
import pytesseract
import tkinter as tk
import argparse
 
#argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--toReader", required=True, help="path to image")
args = vars(ap.parse_args())

# Include tesseract executable in your path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Create an image object of PIL library
image = Image.open(args["toReader"])
 
# pass image into pytesseract module
image_to_text = pytesseract.image_to_string(image, lang='eng')

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

display.mainloop()
>>>>>>> 3d002e980564929c97667330a07cecf18f15ce38
