#!/bin/bash

chmod u+x deploy.sh

wget https://developer.download.nvidia.com/compute/cuda/12.1.0/local_installers/cuda_12.1.0_530.30.02_linux.run
sudo sh cuda_12.1.0_530.30.02_linux.run

# This script is used to deploy the API to the server
pip install --upgrade pip
pip install -r requirements.txt