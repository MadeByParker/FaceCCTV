import shapely.geometry
import shapely.affinity
import cv2

def get_bounding_box(left, top, width, height):
    return shapely.geometry.box(left, top, left + width, top + height)

def get_bounding_box_map(path, **kwargs):
      file_opener = kwargs["open"] if "open" in kwargs.keys() else open

      bounding_box_map = {}

      with file_opener(path) as file:
            data = file.readlines()[2:]

            for line in data:
                  tokens = line.split()

                  file_name = tokens[0]
                  int_tokens = [int(token) for token in tokens[1:]]

                  bounding_box_map[file_name] = get_bounding_box(*int_tokens)

      return bounding_box_map

def bounding_box_iou(box1, box2):
      intersection_box = box1.intersection(box2)
      union_box = box1.union(box2)

      return intersection_box.area / union_box.area

def get_scale(bounding_box, target_size):
      
      horizontal_side = bounding_box.bounds[2] - bounding_box.bounds[0]
      vertical_side = bounding_box.bounds[3] - bounding_box.bounds[1]

      smaller_side = horizontal_side if horizontal_side < vertical_side else vertical_side

      return target_size / smaller_side

def get_scaled_bounding_box(bounding_box, scale):
      return shapely.affinity.affine_transform(bounding_box, [scale, 0, 0, scale, 0, 0])

def flip_bounding_box_y_axis(bounding_box, image_shape):

      bounds = bounding_box.bounds
      return shapely.geometry.box(image_shape[1] - bounds[2], bounds[1], image_shape[1] - bounds[0], bounds[3])

def draw_bounding_box(image, bounding_box, color, thickness):
      bounds = [round(value) for value in bounding_box.bounds]
      cv2.rectangle(image, (bounds[0], bounds[1]), (bounds[2], bounds[3]), color, thickness)