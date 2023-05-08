#!/bin/bash

chmod u+x deploy.sh

wget https://developer.download.nvidia.com/compute/cuda/12.1.0/local_installers/cuda_12.1.0_530.30.02_linux.run
sudo sh cuda_12.1.0_530.30.02_linux.run

# Install production dependencies.
pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt

# Install the dependencies
sudo apt-get install python3-pip python3-dev python3-venv
sudo apt-get install libgl1-mesa-glx

# Run individual install commands
pip install fastapi --no-cache-dir
pip install uvicorn --no-cache-dir
pip install python-multipart --no-cache-dir
pip install aiofiles --no-cache-dir
pip install Pillow --no-cache-dir
pip install opencv-python --no-cache-dir
pip install scikit-image --no-cache-dir
pip install scikit-learn --no-cache-dir
pip install matplotlib --no-cache-dir
apt-get update -y
apt-get install libgl1 -y
apt-get install ffmpeg libsm6 libxext6  -y