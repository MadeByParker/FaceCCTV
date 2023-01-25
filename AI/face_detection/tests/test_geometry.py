import mock

import shapely.geometry

from ..facecctv_ai import geometry

def test_get_bounding_box(self):

      left = 10
      top = 20
      width = 5
      height = 10

      expected_bounding_box = shapely.geometry.box(10, 20, 15, 30)
      actual_bounding_box = geometry.get_bounding_box(left, top, width, height)

      assert expected_bounding_box.equals(actual_bounding_box)

def test_get_bounding_box_map(self):
      file_lines = "101420\nimage_id x_2 y_2 width height\n101420.jpg    95 71 255 242\n102069.jpg    82 104 242 327\n"
      mock_opener = mock.mock_open(read_data=file_lines)

      kwargs = {"open": mock_opener}

      first_bounding_box = shapely.geometry.box(95, 69, 95 + 255, 71 + 242)
      second_bounding_box = shapely.geometry.box(82, 104, 82 + 242, 104 + 327)

      expected_bounding_box_map = {
            "101420.jpg": first_bounding_box, 
            "102069.jpg": second_bounding_box
      }

      actual_bounding_box_map = shapely.geometry.box("whatever", **kwargs)

      assert "101420.jpg" in expected_bounding_box_map
      assert "102069.jpg" in expected_bounding_box_map

      assert first_bounding_box.equals(actual_bounding_box_map["101420.jpg"])
      assert second_bounding_box.equals(actual_bounding_box_map["102069.jpg"])

def test_iou_simple_intersection():

      first_polygon = shapely.geometry.box(10, 10, 20, 20)
      second_polygon = shapely.geometry.box(10, 10, 15, 15)

      assert 0.25 == geometry.iou(first_polygon, second_polygon)
      assert 0.25 == geometry.iou(second_polygon, first_polygon)

def test_iou_simple_no_intersection():

      first_polygon = shapely.geometry.box(10, 10, 20, 20)
      second_polygon = shapely.geometry.box(100, 100, 150, 150)

      assert 0 == geometry.iou(first_polygon, second_polygon)
      assert 0 == geometry.iou(second_polygon, first_polygon)

def test_get_scale_horizontal_box():

      box = shapely.geometry.box(10, 20, 50, 30)
      target_size = 5

      assert 0.5 == geometry.get_scale(box, target_size)

def test_get_scale_vertical_box():

      box = shapely.geometry.box(10, 20, 50, 10)
      target_size = 10

      assert 0.25 == geometry.get_scale(box, target_size)

def test_get_scale_long_box():

      box = shapely.geometry.box(10, 20, 50, 30)
      scale = 3

      expected_scale = shapely.geometry.box(30, 60, 150, 90)
      actual_scale = geometry.get_scaled_bounding_box(box, scale)

      assert expected_scale.equals(actual_scale)

def test_get_scale_tall_box():

      box = shapely.geometry.box(10, 20, 50, 100)
      scale = 0.5

      expected_scale = shapely.geometry.box(5, 10, 25, 50)
      actual_scale = geometry.get_scale(box, scale)

      assert expected_scale.equals(actual_scale)

def test_flip_bounding_box_left_of_y_axis():

      box = shapely.geometry.box(10, 20, 60, 40)
      image_shape = [200, 100]

      expected_flip = shapely.geometry.box(40, 20, 90, 40)
      actual_flip = geometry.flip_bounding_box_y_axis(box, image_shape)

      assert expected_flip.equals(actual_flip)

def test_flip_bounding_box_riht_of_y_axis():

      box = shapely.geometry.box(10, 20, 60, 40)
      image_shape = [200, 80]

      expected_flip = shapely.geometry.box(10, 10, 50, 50)
      actual_flip = geometry.flip_bounding_box_y_axis(box, image_shape)

      assert expected_flip.equals(actual_flip)

def test_flip_bounding_box_center_of_y_axis():

      box = shapely.geometry.box(30, 10, 90, 90)
      image_shape = [200, 120]

      expected_flip = box
      actual_flip = geometry.flip_bounding_box_y_axis(box, image_shape)

      assert expected_flip.equals(actual_flip)