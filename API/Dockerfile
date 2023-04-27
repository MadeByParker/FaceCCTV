# 
FROM python:3.9

WORKDIR /src

ADD ./ /src

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#
RUN pip3 install torch torchvision torchaudio
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
RUN pip install tqdm --no-cache-dir

EXPOSE 8000 

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]