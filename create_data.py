import os
import sys
import glob
import numpy as np
from PIL import Image


word_dir = "words/"
true_dir = "data/true/"
false_dir = "data/false/"

title = int(input("what is the title?"))

def combine(directory, title):
    for other_dir in os.listdir(word_dir):
        if other_dir == '.DS_Store':
            continue
        elif directory != (word_dir + other_dir):
            continue
        for i, j in zip(reversed(os.listdir(directory)), range(len(os.listdir(word_dir + other_dir)))):
            j = (j + 10) % len(os.listdir(word_dir + other_dir))
            j = os.listdir(word_dir + other_dir)[j]
            print(i, j, "zip")
            if i == '.DS_Store' or j == '.DS_Store':
                continue
            elif directory == (word_dir + other_dir):
                title = together(directory + '/' + i, word_dir + other_dir + '/' + j, True, title)
            else:
                title =  together(directory + '/' +  i, word_dir + other_dir + '/' + j, False, title)

    print("Done with folder {} \nMoving to overflow to help prevent repeats".format(directory))
    os.system("mv {} ../overflow/".format(directory))
    
    return title
    
def together(img1, img2, label, title):
    
    img1 = Image.open(img1)
    img2 = Image.open(img2)
    widths, heights = [img1.size[0], img2.size[0]], [img1.size[1], img2.size[1]]
    
    for i in widths:
        if i < 20:
            return title
    
    img1 = img1.resize((128, 32))
    img2 = img2.resize((128, 32))
    widths, heights = [img1.size[0], img2.size[0]], [img1.size[1], img2.size[1]]
    
    total_width = sum(widths)
    max_height = max(heights)

    new_img = Image.new('RGB', (total_width, max_height))

    x_offset = 0

    new_img.paste(img1, (x_offset, 0))
    x_offset += img1.size[0]
    
    new_img.paste(img2, (x_offset, 0))


    if label:
        new_img.save(true_dir + str(title) + '.png')
    else:
        new_img.save(false_dir + str(title) + '.png')
    
    print(title, label)
    title += 1
    return title

for i in os.listdir(word_dir):
    print(i)

    if i == '.DS_Store':
        continue
    else:
        
        ###
        # For removing blank folders
        #if len(os.listdir(word_dir + i + '/')) == 0:
        #    os.system("rm -rf {}".format(word_dir + i))
        ###

        ###
        # For simplifying the folders 
        #os.system("mv {} {}".format(word_dir + i + '/' + ii, word_dir))
        ###

        print("Combining", word_dir +  i)
        title = combine((word_dir + i), title)
 
