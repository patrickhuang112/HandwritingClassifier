# Import modules
from PIL import Image, ImageTk
import PIL
import pytesseract
import tkinter as tk
 
# Include tesseract executable in your path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
 
# Create an image object of PIL library
image = Image.open('TestImage.jpg')
 
# pass image into pytesseract module
# pytesseract is trained in many languages
image_to_text = pytesseract.image_to_string(image, lang='eng')
 
# Print the text
#print(image_to_text)

display = tk.Tk()
display.title("Text Reader")

result = tk.Label(display, text=image_to_text, padx=5, pady=5)
result.grid(column=0, row=0)

path = "TestImage.jpg"
#Image 1
img1 = Image.open('TestImage.jpg')
img1 = img1.resize((200, 200), PIL.Image.ANTIALIAS)
img1.save('TestImage.jpg')
img1 = ImageTk.PhotoImage(Image.open(path))

panel = tk.Label(display, image = img1)
panel.grid(column=1, row=0)

display.mainloop()
