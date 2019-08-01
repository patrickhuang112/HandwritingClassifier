# HandwritingClassifier

The Graphology A.P.E was a project by Allie Surprise, Emily Becher, Griffin Walraven and Patrick Huang for the Northwest Advanced Programming Workshop from July 15th to August 2nd. The project was focused on creating and training a neural network that could analyze two different handwriting samples and predict whether the two samples were written by the same person. 

# Neural Network timeline

The first two networks were 

The team first created a simple neural network for the project. The network would resize all data into 32x32 sized images and flatten them into 1x1024 image. The flattened image would be fed into an input layer with 1024 neurons and go through two hidden layers with 512 and 256 neurons respectively before being output into a final layer with two different possible results: 'true' or 'false'. The main problem with the simple neural network was that it overfitted according to the training data. It was highly effective at predicting true vs false using different samples from the training set. However, testing the simple neural network using samples written by team members exposed the overfitting tendency of the network. 

This neural network was eventually replaced by a convolutional neural network. The team sought to implemenet a convolutional network to increase the reliability and accuracy of the network. The advatage of a convolutional network is that it would analyze sections of the input data instead of individual pixels, granting a stronger ability in recognizing patterns within images. The convolutional network was successful in lessening the overfitting from the simple network. However, it was still prone to inaccurate results as a result from overfitting and reliance on the training data.


# Features

The team created a website and a graphical user interface (GUI) to allow users to test out the neural network in a simple way. Both the website and the GUI has a "predict" tab where users can test out the neural network. Users upload two different images of handwritten words or letters and then click the "Submit" button. When using the website, the two images will be combined and will redisplay on the website with a "true" or "false" prediction along with a prediction certainty percentage. When using the GUI, the user will also have to submit images using the same process. However, the new combined image will display in a new window along with the prediction results.

The team also implemented the pytesseract library which allows analysis of words within images. Within the website and GUI, a user is able to upload an image with handwritten or typed words and the Graphology APE will analyze the image and return with the words it reads in the image. There is also a word find feature where instead of returning all words found within an image, GAPE will return the number of instances of a specific user-defined word. 


# Packages Needed to Run

Python 3 (recommend python 3.6.#)

### Download pytesseract to path
	Windows: C:/Program Files/Tesseract-OCR/tesseract
	Linux: /usr/bin/tesseract
	Darwin/MacOS: /usr/local/bin/tesseract

### Pip Installs (run website)
- flask
- pillow
	
### Pip Installs (run compare/combine)
- numpy
- tensorflow
- keras
- opencv-python
	
### Pip Installs (run read/find)
- pytesseract

# Those involved
- [allisurp](https://github.com/alliesurp)
- [AWOLASAP](https://github.com/AWOLASAP)
- [EmilyBecher](https://github.com/EmilyBecher)
- [patrickhuang112](https://github.com/patrickhuang112)
