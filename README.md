# ![Nice pic of an ape being drawn](/logo.png?raw=true "Graphology A.P.E.") 
# Graphology A.P.E.

The Graphology A.P.E was a project by Allie Surprise, Emily Becher, Griffin Walraven and Patrick Huang for the Northwest Advanced Programming Workshop from July 15th to August 2nd. The project was focused on creating and training a neural network that could analyze two different handwriting samples and predict whether the two samples were written by the same person. 

# Neural Network timeline

#### The first two networks: 

The team first created a simple neural network for the project. The network would resize all data into 32x32 sized images and flatten them into 1x1024 image. The flattened image would be fed into an input layer with 1024 neurons and go through two hidden layers with 512 and 256 neurons respectively before being output into a final layer with two different possible results: 'true' or 'false'. The main problem with the simple neural network was that it overfitted according to the training data. It was highly effective at predicting true vs false using different samples from the training set. However, testing the simple neural network using samples written by team members exposed the overfitting tendency of the network. 

This neural network was eventually replaced by a convolutional neural network. The team sought to implemenet a convolutional network to increase the reliability and accuracy of the network. The advatage of a convolutional network is that it would analyze sections of the input data instead of individual pixels, granting a stronger ability in recognizing patterns within images. The convolutional network was successful in lessening the overfitting from the simple network. However, it was still prone to inaccurate results as a result from overfitting and reliance on the training data.

#### The final network:

The final network we decided upon was a siamese neural network. A siemese network differs from most because it starts out as two seperate but identical networks with two seperate input layers and they merge before the output layer. This is great for comparison tasks such as facial recognition and also useful for one shot learning. This network coupled with a change in our dataset resulted in a model with 84% test accuracy and no overfitting! This network was also the best on user submitted images.

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
	pip install flask
	pip install pillow
	
### Pip Installs (run compare/combine)
	pip install numpy
	pip install tensorflow
	pip install keras
	pip install opencv-python
	
### Pip Installs (run read/find)
	pip install pytesseract

# Running the Website
Location of files is very important to the program so be careful if you move files around. The server runs on port 5555, but this can be changed. To run the server make sure you have the correct packages installed then run this command in the root of the repository:  
	
	python runserver.py
	
# Training the neural networks
If you'd like you can train the neural networks with your own data or change the hyperparemeters you can, just make sure you install the following packages in addition to the prior ones: 
	
	pip install scikit-learn
	pip install pickle
	pip install matplotlib
	pip install imutils
	pip install plaidml 
**Note:** If you are on not on macos then plaidml is not necessary  

The neural networks take a dataset, model location, and plot location as the arguments. e.g. ```python train_simple_nn.py -d data -m simple_nn_network.model -p plot.png``` Datasets are not in the github repository. They can be found at [IAM](http://www.fki.inf.unibe.ch/databases/iam-handwriting-database) We used the words for training the convolutional and simple neural network, and the lines for the siamese dataset.

# Those involved
- [alliesurp](https://github.com/alliesurp)
- [AWOLASAP](https://github.com/AWOLASAP)
- [EmilyBecher](https://github.com/EmilyBecher)
- [patrickhuang112](https://github.com/patrickhuang112)
