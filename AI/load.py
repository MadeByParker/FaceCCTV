import cv2
import os

# Load the annotations file
annotations_path = '/path/to/wider_face_split/wider_face_train_bbx_gt.txt'
annotations = []
with open(annotations_path, 'r') as file:
    for line in file:
        annotations.append(list(map(int, line.strip().split())))
        
# Load the images
images_path = '/path/to/wider_face_split/WIDER_train/images'
images = []
for i, line in enumerate(annotations):
    if i == 0:
        continue
    elif line == []:
        continue
    else:
        image_path = os.path.join(images_path, line[0]+'.jpg')
        image = cv2.imread(image_path)
        images.append(image)
