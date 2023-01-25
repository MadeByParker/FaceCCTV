import numpy as np
import sys
sys.path.append('../')

from ..facecctv_ai import processing

def test_scale_image_height_with_ratio():

      image = np.zeros(shape=[10, 20])
      target_size = 30

      # Height decrease
      rescaled_image = processing.scale_image(image, target_size)

      assert (30, 60) == rescaled_image.shape

def test_scale_image_width_with_ratio():

      image = np.zeros(shape=[10, 5])
      target_size = 20

      # Width decrease
      rescaled_image = processing.scale_image(image, target_size)

      assert (40, 20) == rescaled_image.shape

def test_get_scaled_image_square():

      image = np.zeros(shape=[10, 10])
      scale = 2

      # Height increase
      scaled_image = processing.scale_image(image, scale)

      assert (20, 20) == scaled_image.shape

def test_get_scaled_image_horizontal():

      image = np.zeros(shape=[10, 20])
      scale = 0.5

      # Width decrease
      scaled_image = processing.scale_image(image, scale)

      assert (5, 10) == scaled_image.shape

def test_get_scaled_image_vertical():

      image = np.zeros(shape=[20, 10])
      scale = 0.5

      # Height decrease
      scaled_image = processing.scale_image(image, scale)

      assert (10, 5) == scaled_image.shape

def test_get_smallest_face_in_min_size():

      image_shape = [100, 200]
      min_face_size = 50
      min_face_size_to_image_ratio = 0.1

      expected_face_size = 50
      actual_face_size = processing.get_smallest_face_size(image_shape, min_face_size, min_face_size_to_image_ratio)

      assert expected_face_size == actual_face_size

def test_get_smallest_face_in_min_size_in_image_horizontal():

      image_shape = [100, 50]
      min_face_size = 1
      min_face_size_to_image_ratio = 0.1

      expected_face_size = 5
      actual_face_size = processing.get_smallest_face_size(image_shape, min_face_size, min_face_size_to_image_ratio)

      assert expected_face_size == actual_face_size

def test_get_smallest_face_in_min_size_in_image_vertical():

      image_shape = [200, 500]
      min_face_size = 1
      min_face_size_to_image_ratio = 0.1

      expected_face_size = 20
      actual_face_size = processing.get_smallest_face_size(image_shape, min_face_size, min_face_size_to_image_ratio)

      assert expected_face_size == actual_face_size

def test_get_smallest_face_3D():
      
      image_shape = [200, 500, 3]
      min_face_size = 1
      min_face_size_to_image_ratio = 0.1

      expected_face_size = 20
      actual_face_size = processing.get_smallest_face_size(image_shape, min_face_size, min_face_size_to_image_ratio)

      assert expected_face_size == actual_face_size