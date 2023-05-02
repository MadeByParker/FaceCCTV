# FaceCCTV Setup and Walkthrough instructions

This document will explain how FaceCCTV's architecture works on each platform and an installation guide step by step

## Setup

### Web App

The web app is hosted on a domain so it requires no user interaction.

The domain is <b>https://facecctv.co.uk/</b>

### AI Model

The AI Model is in the AI section of the repository under face_detection which is a singular h5 file to allow it to be store as it has multiple layers and arrays of data. If you want to run it locally for curiousity, it is advised not to run to jupyter notebook as the training process will take a day or two to complete. Use the command `pip install -r requirements.txt` to install the python modules that the AI Model uses.

### API 

The API folder has the most up to date version of the h5 model file and hosted on a server. you can run it locally for experimental use.  First you need to download the `Web-App-and-API.zip` file from the latest release. Once downloaded, extract the content, and place the FaceCCTV folder wherever you want. Using a CLI such as Git Bash, Terminal or Powershell, cd into the FaceCCTV/API/ directory and run the `pip install -r requirements.txt` command to install the python modules that FaceCCTV's API uses. Once done, run the `uvicorn main:app --reload` command to start the server. The API will try to get the local IP of your device and output it, but if it fails to do so, you might have to find the IP address on your own in order to use FaceCCTV on other devices.

By default, port `8000` is used.

#### Web App local use

After following the instructions above, you should be able to use the web app immediately by simply going to the IP address of the host device (or http://127.0.0.1:3000 / http://localhost:3000 if using the host device itself to access it).

### Desktop App

Download the latest version of the desktop app for the platform of your choice from the Releases section, and install it. Once installed, open the app, and then the API should be connected automatically based on the third party server hosting the API.

## Walkthrough on the use of the app

1. Go to <b>https://facecctv.co.uk</b> if using the web app. If using the desktop app, run the `.exe` file downlaod from the web app ot in the Releases section.

You should see the <b>Home Page</b>

![Home Page](https://github.com/Parker06/FaceCCTV/blob/main/Screenshots/Main.png)

2. Drag and drop your image in the upload button or simply click to upload. It accepts .jpeg, .jpg and .png.

![Uploading](https://imgur.com/L9ZJSjZ.jpeg)

3. It may take a few seconds to run the AI through the API. Afterwards it will redirect you to the results page where you can download the result as a .jpeg or .png

![Result](https://github.com/Parker06/FaceCCTV/blob/main/Screenshots/Result.jpg)

Notes:

* The Face Detection and Image Enhancement Pages follow the same procedure.
* The user settings only change on your device so if it's a new device then you will have to set up again.
