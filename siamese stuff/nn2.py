from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Dropout, Activation, Dense
from keras.layers import Add, Flatten, Reshape
from keras.models import Sequential, Model
from keras import backend as K
from keras.optimizers import SGD

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.metrics import classification_report

from imutils import paths

from matplotlib import pyplot as plt

import numpy as np
import argparse
import random
import cv2
import os
import sys


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

def create_model(width, height, depth, classes):

    input_shape = (height, width, depth)

    model1 = Sequential(layers=[
        # input layers and convolutional layers
        Conv2D(32, (3, 3), padding='same', input_shape=input_shape),
        Activation('relu'),
        BatchNormalization(axis=-1),
        MaxPooling2D(pool_size=(3, 3)),
        Dropout(0.2),
        
        Conv2D(64, (6, 6), padding="same"),
	Activation("relu"),
	BatchNormalization(axis=-1),
	Conv2D(64, (6, 6), padding="same"),
	Activation("relu"),
	BatchNormalization(axis=-1),
	MaxPooling2D(pool_size=(3, 3)),
	Dropout(0.2),

    ])
    
    model2 = Sequential(layers=[
        # input layers and convolutional layers
        Conv2D(32, (3, 3), padding='same', input_shape=input_shape),
        Activation('relu'),
        BatchNormalization(axis=-1),
        MaxPooling2D(pool_size=(3, 3)),
        Dropout(0.2),
        
        Conv2D(64, (6, 6), padding="same"),
	Activation("relu"),
	BatchNormalization(axis=-1),
	Conv2D(64, (6, 6), padding="same"),
	Activation("relu"),
	BatchNormalization(axis=-1),
	MaxPooling2D(pool_size=(3, 3)),
	Dropout(0.2),


    ])


    mergedOut = Add()([model1.output, model2.output])
    mergedOut = Flatten()(mergedOut)
    mergedOut = Dense(128, activation='relu')(mergedOut)
    mergedOut = Dropout(0.35)(mergedOut)
    mergedOut = Dense(64, activation='relu')(mergedOut)
    mergedOut = Dropout(0.2)(mergedOut)

    # output layer
    mergedOut = Dense(2, activation='sigmoid')(mergedOut)

    model = Model([model1.input, model2.input], mergedOut)
    print(model.summary())
    return model 

###########################################################################

def slice_image(image):
    slice_1, slice_2 = np.split((np.array(image)), 2, axis=1)
    return slice_1, slice_2

###########################################################################


# initialize the data and labels
print("[INFO] loading images...")
data = [[], []]
labels = []

# grab the folders paths and randomly shuffle them
imagePaths = sorted([os.listdir(args["dataset"] + '/' + 'true'), os.listdir(args['dataset'] + '/' + 'false')])
random.seed(42)
random.shuffle(imagePaths)

x = -1
for i in imagePaths:
    x += 1
    for ii in i:
        if ii == ".DS_Store":
            imagePaths[x].remove(ii)


#control how many images get loaded
amount = 0
x = 0
y = 0

# loop over the input images
for imagePath in imagePaths[0]:
    amount += 1
    if amount > 500:
        break

    n = np.random.randint(2)
    try:
        if n == 1:
            imagePath1 = args["dataset"] + '/true/' + imagePaths[0][x] + '/' + (os.listdir(args["dataset"] + '/true/' + imagePaths[0][x]))[-1]
            imagePath2 = args["dataset"] + '/true/' + imagePaths[0][x] + '/' + (os.listdir(args["dataset"] + '/true/' + imagePaths[0][x]))[-2]
            imagePath3 = args["dataset"] + '/true/' + imagePaths[0][x] + '/' + (os.listdir(args["dataset"] + '/true/' + imagePaths[0][x]))[-3]
            imagePath4 = args["dataset"] + '/true/' + imagePaths[0][x] + '/' + (os.listdir(args["dataset"] + '/true/' + imagePaths[0][x]))[-4]
            x += 1
        else:
            imagePath1 = args["dataset"] + '/false/' + imagePaths[1][y*2]
            imagePath2 = args["dataset"] + '/false/' + imagePaths[1][y*2+1]
            y += 1
    except IndexError:
        break
    
    # load the image, resize it to the required input
    # spatial dimensions of the network, and store the image in the
    # data list
    image1 = cv2.imread(imagePath1)
    image1 = cv2.resize(image1, (256, 64))
    data[0].append(image1)
    
    image2 = cv2.imread(imagePath2)
    image2 = cv2.resize(image2, (256, 64))
    data[1].append(image2)

    # extract the class label from the 
    # image path and update the labels list
    label = "true" if n == 1 else "false"
    if label == "true":
        labels.append(label)
        labels.append(label)
    else:
        labels.append(label)

data = np.array(data)
labels = np.array(labels)

x1 = np.array(data[0])
x2 = np.array(data[1])

# scale the raw pixel intensities to the range [0, 1]
x1 = np.array(x1, dtype="float") / 255.0
x2 = np.array(x2, dtype="float") / 255.0
labels = np.array(labels)

# partition the data into training and testing splits using 75% of
# the data for training and the remaining 25% for testing
(trainx1, testx1, trainY, testY) = train_test_split(x1,
	labels, test_size=0.25, random_state=42)
(trainx2, testx2, trainY, testY) = train_test_split(x2,
	labels, test_size=0.25, random_state=42)

print(trainx1, testx1)
print(trainx2, testx2)
print()
print(trainY, testY)

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
model = create_model(256, 64, 3, classes)
print("Succesfully created model")

EPOCHS = 50
BATCH_SIZE = 16
LEARNING_RATE = 0.01

print("Compiling model")
opt = SGD(lr=LEARNING_RATE)
model.compile(loss="binary_crossentropy", optimizer=opt, metrics=["accuracy"])
print("Succesfully compiled model")

print("Fitting model")
H = model.fit(x=[trainx1, trainx2], y=trainY, batch_size=BATCH_SIZE, epochs=EPOCHS, validation_data=([testx1, testx2], testY))
print("Succesfully fitted model")

# evaluate the network
print("[INFO] evaluating network...")
predictions = model.predict([testx1, testx2], batch_size=BATCH_SIZE)
print(classification_report(testY.argmax(axis=1),
	predictions.argmax(axis=1), target_names=['true', 'false']))

print("[INFO] serializing network and label binarizer...")
model.save(args["model"])


# plot the training loss and accuracy
N = np.arange(0, EPOCHS)
plt.style.use("ggplot")
plt.figure()
plt.plot(N, H.history["loss"], label="train_loss")
plt.plot(N, H.history["val_loss"], label="val_loss")
plt.plot(N, H.history["acc"], label="train_acc")
plt.plot(N, H.history["val_acc"], label="val_acc")
plt.title("Training Loss and Accuracy (Simple NN)")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()
plt.savefig(args["plot"])
