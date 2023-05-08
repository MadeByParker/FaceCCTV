# Development Process of  the AI Model.

1.  Preparing the dataset: A image dataset should have images and respective annotations (bounding box coordinates, height and width). 

2. Preprocessing the data: preprocess the images before feeding them into the CNN. This can include resizing the images, normalizing the pixel values, and applying data augmentation techniques such as random cropping and flipping to increase the diversity of the training data.

3. Building the CNN: This is where we defined our Model Architecture and built it using a pre existing backbone before adding on convolutional layers to specialise the model for face detection.

4. Training the CNN: 
- Split the dataset into training, validation, and testing sets. 

- Train the CNN on the training set using backpropagation and gradient descent to minimize the loss function. 

- Validation set to monitor the performance of the CNN during training and adjust the hyperparameters accordingly. 

- Finally, evaluate the performance of the CNN on the testing set to measure its accuracy and other metrics.
5. Fine-tuning the CNN: Fine-tune the CNN by using transfer learning.

6. Deploy the CNN: Once trained the CNN and achieved satisfactory performance, deploy it in a real-world application for face detection. We will save the file as a h5 or xml file to be used on a API.