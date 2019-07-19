import numpy as np
from PIL import Image
import PIL

list_im = ['photos/1.jpg', 'photos/3.jpg']
imgs    = [ PIL.Image.open(i) for i in list_im ]
# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

# save that beautiful picture
imgs_comb = PIL.Image.fromarray( imgs_comb)
imgs_comb.save( 'finalimage.jpg' )    
img = Image.open('finalimage.jpg')
img = img.resize((64,64))
img.save( 'finalimage.jpg' )    
