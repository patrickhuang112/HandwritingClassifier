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
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.3),
        
        Conv2D(64, (6, 6), padding="same"),
	Activation("relu"),
	BatchNormalization(axis=-1),
	Conv2D(64, (6, 6), padding="same"),
	Activation("relu"),
	BatchNormalization(axis=-1),
	MaxPooling2D(pool_size=(2, 2)),
	Dropout(0.4),

    ])
    
    model2 = Sequential(layers=[
        # input layers and convolutional layers
        Conv2D(32, (3, 3), padding='same', input_shape=input_shape),
        Activation('relu'),
        BatchNormalization(axis=-1),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.3),
        
        Conv2D(64, (6, 6), padding="same"),
	Activation("relu"),
	BatchNormalization(axis=-1),
	Conv2D(64, (6, 6), padding="same"),
	Activation("relu"),
	BatchNormalization(axis=-1),
	MaxPooling2D(pool_size=(2, 2)),
	Dropout(0.4),


    ])


    mergedOut = Add()([model1.output, model2.output])
    mergedOut = Flatten()(mergedOut)
    mergedOut = Dense(128, activation='relu')(mergedOut)
    mergedOut = Dropout(0.5)(mergedOut)
    mergedOut = Dense(64, activation='relu')(mergedOut)
    mergedOut = Dropout(0.35)(mergedOut)

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
data = []
labels = []

# grab the image paths and randomly shuffle them
imagePaths = sorted(list(paths.list_images(args["dataset"])))
random.seed(42)
random.shuffle(imagePaths)

#control how many images get loaded
amount = 0

# loop over the input images
for imagePath in imagePaths:
    amount += 1
    if amount > 100000:
        break
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

trainX_1 = []
trainX_2 = []
testX_1 = []
testX_2 = []

for img in trainX:
    i1, i2 = slice_image(img)
    trainX_1.append(i1)
    trainX_2.append(i2)

for img in testX:
    i1, i2 = slice_image(img)
    testX_1.append(i1)
    testX_2.append(i2)

trainX_1 = np.array(trainX_1)
trainX_2 = np.array(trainX_2)

testX_1 = np.array(testX_1)
testX_2 = np.array(testX_2)


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
model = create_model(32, 32, 3, classes)
print("Succesfully created model")

EPOCHS = 30
BATCH_SIZE = 64
LEARNING_RATE = 0.01

print("Compiling model")
opt = SGD(lr=LEARNING_RATE)
model.compile(loss="binary_crossentropy", optimizer=opt, metrics=["accuracy"])
print("Succesfully compiled model")

print("Fitting model")
H = model.fit(x=[trainX_1, trainX_2], y=trainY, batch_size=BATCH_SIZE, epochs=EPOCHS, validation_data=([testX_1, testX_2], testY))
print("Succesfully fitted model")

# evaluate the network
print("[INFO] evaluating network...")
predictions = model.predict([testX_1, testX_2], batch_size=BATCH_SIZE)
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
