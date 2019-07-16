from PIL import Image

size = 64, 64


image = Image.open('photos/word1(1).png')
image.thumbnail(size, Image.ANTIALIAS)
image.save('word1(1).jpg', "JPEG")

