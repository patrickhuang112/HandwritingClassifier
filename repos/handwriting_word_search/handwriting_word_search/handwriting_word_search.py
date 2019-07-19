#Handwritten Word Search using pytesseract

# Import modules
import PIL
from PIL import Image, ImageTk
import pytesseract
import tkinter as tk
from tkinter import ttk

 
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


display = tk.Tk()
display.title("Word Finder")



result = tk.Label(display, text=image_to_text, padx=5, pady=5)

result.grid(column=0, row=0)



path = "TESTimage.gif"

#Image 1

img1 = Image.open('TESTimage.gif')

img1 = img1.resize((200, 200), PIL.Image.ANTIALIAS)

img1.save('TESTimage.gif')

img1 = ImageTk.PhotoImage(Image.open(path))



panel = tk.Label(display, image = img1)

panel.grid(column=1, row=0)



display.mainloop()

