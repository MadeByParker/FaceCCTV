# Use the official lightweight Python image.
FROM python:3.9-slim as py

# Allow statements and log 
FROM py as base
ENV PYTHONUNBUFFERED 1

# Copy local code to the container image.
WORKDIR /app
COPY requirements.txt /app
COPY . /app

# Install production dependencies.
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Run individual install commands
RUN pip install fastapi --no-cache-dir
RUN pip install uvicorn --no-cache-dir
RUN pip install python-multipart --no-cache-dir
RUN pip install aiofiles --no-cache-dir
RUN pip install Pillow --no-cache-dir
RUN pip install opencv-python --no-cache-dir
RUN pip install scikit-image --no-cache-dir
RUN pip install scikit-learn --no-cache-dir
RUN pip install matplotlib --no-cache-dir
RUN pip install pandas --no-cache-dir
RUN pip install numpy --no-cache-dir
RUN pip install tensorflow --no-cache-dir
RUN pip install tqdm --no-cache-dir
RUN apt-get update && apt-get install libgl1 -y
RUN apt-get install ffmpeg libsm6 libxext6  -y

EXPOSE 8000
 
# Run
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "15400"]

