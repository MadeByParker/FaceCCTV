# FaceCCTV AI Model

This section hosts the development of the FaceCCTV AI Model. Read the README in the main repository to learn more.

### The Model itself

This model is a Deep Learning Model to detect faces and then crop, enhance and colourise them. The model contains two losses before it is trained

1. There's a classification loss which is using Binary Crossentropy loss and that's how the model detects whether an image has a face or not (outcomes being 0 and 1).

2. The detected faces will have a bounding box around them similar to the labeled dataset. They will be drawn by extracting 2 opposite coordinates (top left and bottom right or vice versa). To estimate how close our predicted coordinates to the actual coordinates, the model will use localisation loss.

3. We'll be using the Tensorflow Keras Function API to classify the faces (using their VGG16 pre-trained AI)

### Dataset

- Dataset [link here to Google Drive](https://drive.google.com/drive/folders/1Y11KhmhUfg3q6JRAv4idBBt-OuFEvQBv?usp=sharing)

### Resources

### AI Face Detection

| Resource                        | URL                                                                        |
| ------------------------------- | -------------------------------------------------------------------------- |
| Imutils                         | [Github](https://github.com/PyImageSearch/imutils)                         |
| Labelme - Image Annotation Tool | [Github](https://github.com/wkentaro/labelme)                              |
| Matplotlib                      | [Website](https://matplotlib.org/stable/users/installing/index.html)       |
| NumPy                           | [Website](https://numpy.org)                                               |
| OpenCV                          | [Website](https://opencv.org) / [Github](https://github.com/opencv/opencv) |
| Scikit-learn                    | [Website](https://scikit-learn.org/stable/)                                |
| Split-Folders                   | [Github](https://github.com/jfilter/split-folders)                         |
| Tensorflow                      | [Website](https://www.tensorflow.org)                                      |
| Tensorflow-GPU                  | [Website](https://pypi.org/project/tensorflow-gpu/)                        |
| Tensorflow-keras                | [Website](https://keras.io/getting_started/)                               |

### AI Image Enhancement

| Resource            | URL                                                                                           |
| ------------------- | --------------------------------------------------------------------------------------------- |
| ESRGAN              | [Github](https://github.com/xinntao/ESRGAN)                                                   |
| ESRGAN Neural Model | [Google Drive Link](https://drive.google.com/drive/folders/17VYV_SoZZesU6mbxz2dMAIccSSlqLecY) |
| Glob2               | [Github](https://github.com/miracle2k/python-glob2/)                                          |
| OpenCV              | [Website](https://opencv.org) / [Github](https://github.com/opencv/opencv)                    |
| PyTorch             | [Website](https://pytorch.org)                                                                |
