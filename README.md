<a name="readme-top"></a>

![Banner](https://github.com/Parker06/Parker06/blob/main/New%20Banner.jpg)

<br>

# FaceCCTV - AI Tool for CCTV Footage

![Thumbnail](https://github.com/Parker06/FaceCCTV/blob/main/documentation/Showcase/Thumbnail.png)
![Main Page](https://github.com/Parker06/FaceCCTV/blob/main/Screenshots/Main.png)

## Before Reading

This repository contains the source code and assets for my Final Year Project at University.

#### **DISCLAIMER ALERT: This is a piece of software that was made for my final year university project so there might be unintentional bugs with the software or the AI itself so if you are going to use it in real life applications, please be aware that the AI may not perform well for your particular user case.**

### Brief Demo

A brief video has been recorded to show the application running - not done yet (coming soon).

### Setup Instructions

Please see the [following README](./WALKTHROUGH.md) for setup instructions.

<!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About the Project</a>
      <ul>
        <li><a href="#topic-research">Topic Research</a></li>
        <li><a href="#project-research">Project Research</a></li>
        <li><a href="#project-vision">Project Vision</a></li>
      </ul>
    </li>
    <li>
      <a href="#list-of-project-objectives">List of Project Objectives</a>
      <ul>
        <li><a href="#main-objectives">Main Objectives</a></li>
        <li><a href="#side-objectives">Side Objectives</a></li>
      </ul>
    </li>
    <li><a href="#security">Security</a></li>
    <li><a href="#hosting">Hosting</a></li>
    <li>
      <a href="#screenshots">Screenshots</a>
      <ul>
        <li><a href="#web-app">Web App</a></li>
        <li><a href="#desktop-app">Desktop App</li>
      </ul>
    </li>
      <a href="#credits-and-resources">Credits / Resources</a>
      <ul>
        <li><a href="#general">General</a></li>
        <li><a href="#ai-face-detection">AI Face Detection</a></li>
        <li><a href="#ai-image-enhancement">AI Image Enhancement</a></li>
        <li><a href="#api">AI API</a></li>
        <li><a href="#web-app">Web App</a></li>
        <li><a href="#desktop-app">Desktop App</a></li>
        <li><a href="#mobile-app">Mobile App</a></li>
      </ul>
    </li>
  </ol>
</details>

## About the Project

### Topic Research

- Why is the footage on CCTV cameras often bad quality? [click here](https://www.scienceabc.com/eyeopeners/why-is-the-quality-of-cctv-footage-still-so-low.html)
- Youtube Video explaining why CCTV cameras have poor quality. [here](https://www.youtube.com/watch?v=KWCPXJXWum8)
- UK Crime and Safety Statistics [here](https://crimerate.co.uk/#:~:text=The%20crime%20rate%20in%20the,77.49%20crimes%20per%201%2C000%20people.)
- Why are CCTV cameras essential to public safety in the UK? [click here](https://www.calipsa.io/blog/cctv-statistics-in-the-uk-your-questions-answered)

### Project Research

- [How Face Recognition Works in Facebook.](https://zbigatron.com/how-facial-recognition-works-part-1/)
- [Size of training dataset](https://towardsdatascience.com/how-do-you-know-you-have-enough-training-data-ad9b1fd679ee)

### Project Vision

After doing research on the crime rate percentage and seeing a 1% increase of crimes committed in 2021 from 2020 to approximately 79,000 in the last 12 months and only a 5% of those result in a charge. You wonder why? This is partly due to the poor quality of CCTV, which makes finding the right person more difficult. Adding to this, higher-resolution cameras are on the expensive side which most businesses can’t afford, due to high costs or budget restrictions, resulting in them purchasing lower-resolution CCTV cameras which could lead to poor image quality. If you ever tried to upscale an image, it will become very pixelated and may require photo editing skills to do it professionally, which potentially adds to the costs.

My solution is an app called FaceCCTV, where users can upload an image then the app uses deep learning AI (trained beforehand with a dataset of pre-collected images). the AI can detect the faces in an image and then enhance the faces, which the user can export and use later on. The main goal is to provide a tool that is easy to use and powered by AI to help people identify criminals easier without the unnecessary costs of cameras or professionals.

![Poster](https://github.com/Parker06/FaceCCTV/blob/main/documentation/Showcase/Poster.jpg)

### Dataset

- Dataset link [link here to Google Drive](https://drive.google.com/drive/folders/1Y11KhmhUfg3q6JRAv4idBBt-OuFEvQBv?usp=sharing)
- Link to WIDER Face dataset [here](http://shuoyang1213.me/WIDERFACE/)

## List of Project Objectives

### Main Objectives:

- Create an AI that can detect faces or bodies of people.
- Once detected, the AI zooms in on the area and enhances it so the user can see clearly.
- Simple User Interface capable of being used by everyone.

### Side Objectives

- The AI can identify objects such as car registration plates, car models, locations.
- The AI is optimally developed so there aren't any performance issues.
- The AI should be able to handle any image, in size and resolution.
- The Image could be colurised with AI after the enhancement process.

## Security

- As this project handling with very sensitive data, I am not permitted to allow users store CCTV on my website for later use in case of a data breach or if i had the intent to access the data myself as this could conflict with the rules of the Human Rights Act 1998, 2018 GDPR Regulations and etc... [as stated here](https://www.caughtoncamera.net/news/cctv-legal-requirements-cctv-laws-explained/)
- As users can upload images to the website via a mobile network connection or through WiFi, the images will be encrypted in transit (using AES-256-CBC mode) to ensure that unauthorised parties can't intercept whilst uploading/downloading.

## Hosting

The project will be hosted at [facecctv.co.uk](https://facecctv.co.uk) to access the web app and available to download on windows and mobile. The API is hosted on a third party server which stores the latest version of the AI model which is a h5 file.

## Tech Stack

- FaceCCTV AI Model - Python, Jupyter Notebook
- FaceCCTV AI API:  Python, FastAPI
- Web App: HTML, CSS, JavaScript, TailwindCSS
- Desktop App: Electron, HTML, CSS, JavaScript, Tailwind CSS
- Mobile App: React Native, JavaScript

## Screenshots

### Web App

<details>
	<summary><b>Main Page</b></summary>
	<img src="https://github.com/Parker06/FaceCCTV/blob/main/Screenshots/Main.png"/><br>
</details>
<details>
	<summary><b>Showcase</b></summary>
	<img src="https://github.com/Parker06/FaceCCTV/blob/main/Screenshots/Showcase.png"/><br>
</details>
<details>
	<summary><b>Settings</b></summary>
	<img src="https://github.com/Parker06/FaceCCTV/blob/main/Screenshots/Settings.png"/><br>
</details>
<details>
	<summary><b>Face Detection</b></summary>
	<img src="https://github.com/Parker06/FaceCCTV/blob/main/Screenshots/Face-Detection.png"/><br>
</details>
<details>
	<summary><b>Image Enhancement</b></summary>
	<img src="https://github.com/Parker06/FaceCCTV/blob/main/Screenshots/Image-Enhancement.png"/><br>
</details>
<details>
	<summary><b>Uploading</b></summary>
	<img src="https://github.com/Parker06/FaceCCTV/blob/main/Screenshots/Uploading.png"/><br>
</details>
<!--Screenshot Template<details>
	<summary><b></b></summary>
	<img src=""/><br>
</details>-->

### Desktop App

## Credits and Resources

### General

| Resource                      | URL                                                         |
| ----------------------------- | ----------------------------------------------------------- |
| Adobe Color                   | [Website](https://color.adobe.com/create/color-wheel)       |
| Adobe Photoshop 2023          | [Website](https://www.adobe.com/uk/products/photoshop.html) |
| Figma                         | [Website](www.figma.com/)                                   |
| NodeJS                        | [Website](https://nodejs.org/en/)                           |
| Pip - PyPI                    | [Website](https://pypi.org/project/pip/)                    |
| Python                        | [Website](https://www.python.org)                           |
| Visual Studio C++ Build Tools | [Website](https://visualstudio.microsoft.com/downloads/)    |

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

### API

| Resource               | URL                                              |
| ---------------------  | ------------------------------------------------ |
| AWS Web Services       | [Documentation](https://docs.aws.amazon.com)     |
| FastAPI REST Framework | [Website](https://fastapi.tiangolo.com)          |

### Web App

| Resource          | URL                                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------------- |
| Background        | [SVG Backgrounds](https://www.svgbackgrounds.com)                                                 |
| Bootstrap Icons   | [Website](https://icons.getbootstrap.com)                                                         |
| Flowbite          | [Website](https://flowbite.com)                                                                   |
| Font Awesome      | [Website](https://fontawesome.com)                                                                |
| Google Firebase   | [Website](https://firebase.google.com) [Documentation](https://firebase.google.com/docs)          |
| Inter Font Family | [Website](https://rsms.me/inter/) / [Google Font Family](https://fonts.google.com/specimen/Inter) |
| JQuery            | [Website](https://jquery.com)                                                                     |
| Tailwind CSS      | [Website](https://tailwindcss.com)                                                                |

### Desktop App

| Resource      | URL                                   |
| ------------- | ------------------------------------- |
| Same as above |                                       |
| Electron      | [Website](https://www.electronjs.org) |

### Mobile App

| Resource                                  | URL                                                                                    |
| ----------------------------------------- | -------------------------------------------------------------------------------------- |
| @expo/webpack-config                      | [NPM Package](https://www.npmjs.com/package/@expo/webpack-config)                      |
| @react-native-async-storage/async-storage | [NPM Package](https://www.npmjs.com/package/@react-native-async-storage/async-storage) |
| @react-navigation/native                  | [NPM Package](https://www.npmjs.com/package/@react-navigation/native)                  |
| @react-navigation/stack                   | [NPM Package](https://www.npmjs.com/package/@react-navigation/stack)                   |
| @reduxjs/toolkit                          | [NPM Package](https://www.npmjs.com/package/@reduxjs/toolkit)                          |
| Expo                                      | [Website](https://expo.dev)                                                            |
| expo-font                                 | [NPM Package](https://www.npmjs.com/package/expo-font)                                 |
| expo-status-bar                           | [NPM Package](https://www.npmjs.com/package/expo-status-bar)                           |
| expo-updates                              | [NPM Package](https://www.npmjs.com/package/expo-updates)                              |
| React                                     | [Website](https://reactjs.org)                                                         |
| react-dom                                 | [NPM Package](https://www.npmjs.com/package/react-dom)                                 |
| react-native                              | [Website](https://reactnative.dev)                                                     |
| react-native-elements                     | [NPM Package](https://www.npmjs.com/package/react-native-elements)                     |
| react-native-gesture-handler              | [NPM Package](https://www.npmjs.com/package/react-native-gesture-handler)              |
| react-native-safe-area-context            | [NPM Package](https://www.npmjs.com/package/react-native-safe-area-context)            |
| react-native-vector-icons                 | [NPM Package](https://www.npmjs.com/package/react-native-vector-icons)                 |
| react-native-web                          | [NPM Package](https://www.npmjs.com/package/)                                          |
| react-redux                               | [NPM Package](https://www.npmjs.com/package/)                                          |
