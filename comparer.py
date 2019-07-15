import numpy as np

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib
matplotlib.use("TKagg")

from skimage import data, img_as_float
from skimage.measure import compare_ssim as ssim

import PIL
from PIL import Image


def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray

#Resize images to 500 X 500
img1_name = "photos/1.jpg"
img1 = Image.open(img1_name)
img1= img1.resize((500, 500), PIL.Image.ANTIALIAS)
new_name1 = img1_name[:-4] + 'R' + img1_name[-4:]
img1.save(new_name1)

img2_name = "photos/2.jpg"
img2 = Image.open(img2_name)
img2= img2.resize((500, 500), PIL.Image.ANTIALIAS)
new_name2 = img2_name[:-4] + 'R' + img2_name[-4:]
img2.save(new_name2)

img1 = rgb2gray(mpimg.imread(new_name1))

img2 = rgb2gray(mpimg.imread(new_name2))

rows, cols = img1.shape

def mse(x, y):
    return np.linalg.norm(x - y)

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 4),
                         sharex=True, sharey=True)
ax = axes.ravel()

mse_img1 = mse(img1, img1)
ssim_img1 = ssim(img1, img1, data_range=img1.max() - img1.min())

mse_img2 = mse(img1, img2)
ssim_img2 = ssim(img1, img2,
                  data_range=img2.max() - img2.min())

label = 'MSE: {:.2f}, SSIM: {:.2f}'

ax[0].imshow(img1, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[0].set_xlabel(label.format(mse_img1, ssim_img1))
ax[0].set_title(new_name1)

ax[1].imshow(img2, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[1].set_xlabel(label.format(mse_img2, ssim_img2))
ax[1].set_title(new_name2)

plt.tight_layout()
plt.show()
