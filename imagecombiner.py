import numpy as np
from PIL import Image
import PIL
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i1", "--image1", required=True,
	help="path to input image we are going to classify")
ap.add_argument("-i2", "--image2", required=True,
	help="path to second imagel")
ap.add_argument("-o", "--output_name", required=True,
        help="name of final image")
args = vars(ap.parse_args())

list_im = [args["image1"], args["image2"]]
imgs    = [ PIL.Image.open(i) for i in list_im ]
min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

# save that beautiful picture
imgs_comb = PIL.Image.fromarray( imgs_comb)
imgs_comb.save(args["output_name"] + ".jpg")    
