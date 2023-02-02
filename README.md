<a name="readme-top"></a>

![Banner](https://github.com/Parker06/Parker06/blob/main/New%20Banner.jpg)

<br>

# FaceCCTV


[Thumbnail](https://github.com/Parker06/FaceCCTV/blob/main/documentation/Thumbnail.png)

## Before Reading

This repository contains the source code and assets for my Final Year Project at University.

#### **DISCLAIMER ALERT: This is a piece of software that was made for my final year university project so there might be unintentional bugs with the software or the AI itself so if you are going to use it in real life applications, please be aware that the AI may not perform well for your particular user case.**

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
    <li><a href="#other-miscellanous-items">Project Management Planner</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#setup">Setup</a></li>
        <li><a href="#hosting">Hosting</a></li>
      </ul>
    </li>
    <li><a href="#images">Images</a></li>
    <li>
      <a href="#credits-and-resources">Credits / Resources</a>
      <ul>
        <li><a href="#general">General</a></li>
        <li><a href="#ai-face-detection">AI Face Detection</a></li>
        <li><a href="#ai-image-enhancement">AI Image Enhancement</a></li>
		        <li><a href="#ai-api">AI API</a></li>
        <li><a href="#web-app">Web App</a></li>
        <li><a href="#desktop-app">Desktop App</a></li>
        <li><a href="#mobile-app">Mobile App</a></li>
      </ul>
    </li>
  </ol>
</details>

## About the Project

### Topic Research

- Why is the footage on CCTV cameras bad quality? [click here](https://www.scienceabc.com/eyeopeners/why-is-the-quality-of-cctv-footage-still-so-low.html)
- Youtube Video explaining why CCTV camera have poor quality. [here](https://www.youtube.com/watch?v=KWCPXJXWum8)
- UK Crime and Safety Statistics [here](https://crimerate.co.uk/#:~:text=The%20crime%20rate%20in%20the,77.49%20crimes%20per%201%2C000%20people.)
- Why are CCTV cameras essential to public safety in the UK? [click here](https://www.calipsa.io/blog/cctv-statistics-in-the-uk-your-questions-answered)

### Project Research

- [How Face Recognition Works in Facebook.](https://zbigatron.com/how-facial-recognition-works-part-1/)
- [Size of training dataset](https://towardsdatascience.com/how-do-you-know-you-have-enough-training-data-ad9b1fd679ee)

### Project Vision

After doing research on the crime rate percentage and seeing a 1% increase of crimes committed in 2021 from 2020 to approximately 79,000 in the last 12 months and only a 5% of those result in a charge. You wonder why? This is partly due to the poor quality of CCTV, which makes finding the right person more difficult. Adding to this, higher-resolution cameras are on the expensive side which most businesses can’t afford, due to high costs or budget restrictions, resulting in them purchasing lower-resolution CCTV cameras which could lead to poor image quality. If you ever tried to upscale an image, it will become very pixelated and may require photo editing skills to do it professionally, which potentially adds to the costs.

My solution is an app called FaceCCTV, where users can upload an image then the app uses deep learning AI (trained beforehand with a dataset of pre-collected images). the AI can detect the faces in an image and then enhance the faces, which the user can export and use later on. The main goal is to provide a tool that is easy to use and powered by AI to help people identify criminals easier without the unnecessary costs of cameras or professionals.

### Dataset

- Dataset link [link here to Google Drive](https://drive.google.com/drive/folders/1Y11KhmhUfg3q6JRAv4idBBt-OuFEvQBv?usp=sharing)

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

## Other Miscellanous Items

### Project Management Planner

To view my project planner on Jira, please visit [this link](https://id.atlassian.com/invite/p/jira-software?id=Oz8QbbMWRCyVmXMjr2BcFQ).

## Getting Started

### Prerequisites

### Installation

You can download the webs app and the mobile app from their respective sections of this repository. (once it is deployed)

### Setup

## Tech Stack

- FaceCCTV AI Model - Python
- FaceCCTV AI API:  Flask, Python
- Web App: HTML, CSS, JavaScript
- Desktop App: Electron, HTML, CSS, JavaScript
- Mobile App: React Native, JavaScript

## Images (coming soon)

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

### AI API

| Resource      | URL |
| ------------- | --- |
| Python        |     |
| Flask         |     |
| Flask RESTful |     |

### Web App

| Resource          | URL                                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------------- |
| Background        | [SVG Backgrounds](https://www.svgbackgrounds.com)                                                 |
| Bootstrap Icons   | [Website](https://icons.getbootstrap.com)                                                         |
| Flowbite          | [Website](https://flowbite.com)                                                                   |
| Font Awesome      | [Website](https://fontawesome.com)                                                                |
| Inter Font Family | [Website](https://rsms.me/inter/) / [Google Font Family](https://fonts.google.com/specimen/Inter) |
| JQuery            | [Website](https://jquery.com)                                                                     |
| Tailwind CSS      | [Website](https://tailwindcss.com)                                                                |

### Desktop App

| Resource      | URL                                   |
| ------------- | ------------------------------------- |
| Same as above |                                       |
| Electron      | [Website](https://www.electronjs.org) |

### Mobile App

| Resource     | URL                                                     |
| ------------ | ------------------------------------------------------- |
| React Native | [Website](https://reactnative.dev/docs/getting-started) |
