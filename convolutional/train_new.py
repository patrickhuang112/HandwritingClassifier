import numpy as np 
import matplotlib.pyplot as plt 
import os
import cv2 

DATADIR = 'C:/Users/patbh.DESKTOP-U9IFEBL/Downloads/HandwritingClassifier/HandwritingClassifier/classifier/data'
CATEGORIES = ['True', 'False']

for category in CATEGORIES:
	path = os.path.join(DATADIR, category)
	for img in os.listdir(path):
		img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
		plt.imshow(img_array, cmap='gray')
		plt.show()

		break
	break


IMG_SIZE = 32

new_array = cv2.resize(img_array, (IMG_SIZE*4, IMG_SIZE))
plt.imshow(new_array, cmap = 'gray')
plt.show()