import numpy as np
from PIL import Image
import PIL
import argparse
import cv2
import os
import sys

ap = argparse.ArgumentParser()
ap.add_argument("-i1", "--image1", required=True,
	help="path to input image we are going to classify")
ap.add_argument("-i2", "--image2", required=True,
	help="path to second image")
ap.add_argument("-o", "--output_name", required=True,
        help="name of final image")
ap.add_argument("-l", "--launcher", required=False)
args = vars(ap.parse_args())

#Launched by GUI?
launched = "0"
try:
    if args["launcher"] == '1':
        launched = '1'
except:
    pass

print (args["image1"])
list_im = [args["image1"], args["image2"]]
imgs    = [ PIL.Image.open(i) for i in list_im ]
min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

# save that beautiful picture
imgs_comb = PIL.Image.fromarray( imgs_comb)
imgs_comb.save(args["output_name"] + ".jpg")    
img = Image.open(args['output_name'] + '.jpg')
#img = img.resize((32, 32))
img.save(args['output_name'] + '.jpg')

#display that beautiful picture
image = cv2.imread(args['output_name'] + '.jpg')
cv2.imwrite("handwriting_classifier/static/combinedImage.png", image)
cv2.imshow("Combined Image", image)
if launched == '1':
    while 1:
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
