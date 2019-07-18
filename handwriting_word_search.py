#Handwritten Word Search using pytesseract

# Import modules
from PIL import Image
import pytesseract
tkinter
 
# Include tesseract executable in your path
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\galbraithja\AppData\Local\Tesseract-OCR\tesseract.exe"
 
# Create an image object of PIL library
image = Image.open('TESTimage.gif')
 
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
   if lowerword == "and":
       count += 1
if count == 1:
    print("'and' occurs 1 time.")
else:
    print("'and' occurs", count, "time(s)!")

