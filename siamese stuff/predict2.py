# USAGE
# python predict.py --image images/dog.jpg --model output/simple_nn.model --label-bin output/simple_nn_lb.pickle --width 32 --height 32 --flatten 1
# python predict.py --image images/dog.jpg --model output/smallvggnet.model --label-bin output/smallvggnet_lb.pickle --width 64 --height 64

# import the necessary packages
from keras.models import load_model
import argparse
import pickle
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i1", "--image1", required=True,
	help="path to input image we are going to classify")
ap.add_argument("-i2", "--image2", required=True,
	help="path to input image we are going to classify")
ap.add_argument("-m", "--model", required=True,
	help="path to trained Keras model")
#ap.add_argument("-l", "--label-bin", required=True,
	#help="path to label binarizer")
ap.add_argument("-w", "--width", type=int, default=32,
	help="target spatial dimension width")
ap.add_argument("-e", "--height", type=int, default=32,
	help="target spatial dimension height")
ap.add_argument("-f", "--flatten", type=int, default=-1,
	help="whether or not we should flatten the image")
args = vars(ap.parse_args())

# load the input image and resize it to the target spatial dimensions
image1 = cv2.imread(args["image1"])
image2 = cv2.imread(args["image2"])
output1 = image1.copy()
output2 = image2.copy()
image1 = cv2.resize(image1, (args["width"], args["height"]))
image2 = cv2.resize(image2, (args["width"], args["height"]))

# scale the pixel values to [0, 1]
image1 = image1.astype("float") / 255.0
image2 = image2.astype("float") / 255.0

# check to see if we should flatten the image and add a batch
# dimension
if args["flatten"] > 0:
	image = image.flatten()
	image = image.reshape((1, image.shape[0]))

# otherwise, we must be working with a CNN -- don't flatten the
# image, simply add the batch dimension
else:
	image1 = image1.reshape((1, image1.shape[0], image1.shape[1],
		image1.shape[2]))
	image2 = image2.reshape((1, image2.shape[0], image2.shape[1],
		image2.shape[2]))

# load the model and label binarizer
print("[INFO] loading network and label binarizer...")
model = load_model(args["model"])
#lb = pickle.loads(open(args["label_bin"], "rb").read())

# make a prediction on the image
preds = model.predict([image1, image2])

# find the class label index with the largest corresponding
# probability
i = preds.argmax(axis=1)[0]
label = ['False', 'True'][i]
print("got {}".format(label))
with open("handwriting_classifier/static/truefalse.txt", "w+") as f:
    f.write(label)

# draw the class label + probability on the output image
text = "{}: {:.2f}%".format(label, preds[0][i] * 100)
cv2.putText(output1, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
	(0, 0, 255), 2)

# show the output image
cv2.imshow("Image", output1)
cv2.imwrite("Output1.png", output1)

