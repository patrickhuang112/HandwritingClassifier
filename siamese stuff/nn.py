from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Dropout, Activation, Dense
from keras.layers import Add, Flatten
from keras.models import Sequential, Model
from keras import backend as K

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

from imutils import paths

import numpy as np
import argparse
import random
import cv2
import os

#construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset of images")
ap.add_argument("-m", "--model", required=True,
	help="path to output trained model")
ap.add_argument("-p", "--plot", required=True,
	help="path to output accuracy/loss plot")
args = vars(ap.parse_args())

###########################################################################

def create_nn(width, height, depth, classes):

    input_shape = (width, height, depth)

    model1 = Sequential(layers=[
        # input layers and convolutional layers
        Conv2D(32, (3, 3), padding='same', input_shape=input_shape),
        Activation('relu'),
        BatchNormalization(axis=1),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.2),
    ])
    
    model2 = Sequential(layers=[
        # input layers and convolutional layers
        Conv2D(32, (3, 3), padding='same', input_shape=input_shape),
        Activation('relu'),
        BatchNormalization(axis=1),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.2),
    ])


    mergedOut = Add()([model1.output, model2.output])
    mergedOut = Flatten()(mergedOut)
    mergedOut = Dense(256, activation='relu')(mergedOut)
    mergedOut = Dropout(.5)(mergedOut)
    mergedOut = Dense(128, activation='relu')(mergedOut)
    mergedOut = Dropout(.35)(mergedOut)

    # output layer
    Dense(len(classes), activation='softmax')

    model = Model([model1.input, model2.input], mergedOut)
    return model 

###########################################################################

def slice_image(image):
    bbox_1 = (9, 0, 32, 32)
    bbox_2 = (32, 0, 64, 32)
    slice_1 = image.crop(bbox_2)
    slice_2 = image.crop(bbox_2)
    return slice_1, slice_2

###########################################################################


# initialize the data and labels
print("[INFO] loading images...")
data = []
labels = []

# grab the image paths and randomly shuffle them
imagePaths = sorted(list(paths.list_images(args["dataset"])))
random.seed(42)
random.shuffle(imagePaths)

# loop over the input images
for imagePath in imagePaths:
    # load the image, resize it to 64x64 pixels (the required input
    # spatial dimensions of SmallVGGNet), and store the image in the
    # data list
    image = cv2.imread(imagePath)
    image = cv2.resize(image, (64, 32))
    data.append(image)

    # extract the class label from the 
    # image path and update the labels list
    label = imagePath.split(os.path.sep)[-2]
    labels.append(label)

# scale the raw pixel intensities to the range [0, 1]
data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)

# partition the data into training and testing splits using 75% of
# the data for training and the remaining 25% for testing
(trainX, testX, trainY, testY) = train_test_split(data,
	labels, test_size=0.25, random_state=42)
print(trainX.shape)


# convert the labels from integers to vectors (for 2-class, binary
# classification you should use Keras' to_categorical function
# instead as the scikit-learn's LabelBinarizer will not return a
# vector)

le = LabelEncoder()
ohe = OneHotEncoder(sparse=False)
integer_encoded = le.fit_transform(trainY)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
trainY = ohe.fit_transform(integer_encoded)


integer_encoded = le.fit_transform(testY)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
testY = ohe.fit_transform(integer_encoded)
classes = ["true", "false"]


# Create the neural network (width, height, deph, classes)
print("Creating neural network")
create_nn(32, 32, 3, classes)
print("Succesfully created neural network")


