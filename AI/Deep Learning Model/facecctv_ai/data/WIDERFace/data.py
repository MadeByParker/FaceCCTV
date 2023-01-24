"""
Code for working with any dataset
"""

import os
import shutil
import subprocess
import glob

import facecctv_ai.download
import facecctv_ai.utils
import facecctv_ai.geometry


class DatasetBuilder:
    """
    Class for downloading data and preparing datasets from it.
    """

    def __init__(self, data_directory):

        self.data_directory = data_directory
        self.bounding_boxes_path = os.path.join(self.data_directory, "all_bounding_boxes.txt")

    def build_datasets(self):

        shutil.rmtree(self.data_directory, ignore_errors=True)
        os.makedirs(self.data_directory, exist_ok=True)

        self._get_images()
        self._get_bounding_boxes()

        image_paths = self._get_image_paths(self.data_directory)
        bounding_boxes_map = self._get_bounding_boxes_map(self.bounding_boxes_path)

        datasets_dirs = ["large_dataset", "medium_dataset", "small_dataset"]

        large_dataset_split = [0, 180000, 190000, len(image_paths)]
        medium_dataset_split = [0, 10000, 20000, 30000]
        small_dataset_split = [0, 1000, 2000, 3000]

        splits = [large_dataset_split, medium_dataset_split, small_dataset_split]

        for dataset_dir, splits in zip(datasets_dirs, splits):

            directory = os.path.join(self.data_directory, dataset_dir)
            DataSubsetBuilder(directory, image_paths, bounding_boxes_map, splits).build()

    def _get_images(self):

        image_archives_urls = [
            "https://drive.google.com/uc?export=download&id=15hGDLhsx8bLgLcIRD5DhYt5iBxnjNF1M/",
            "https://drive.google.com/uc?export=download&id=1GUCogbp16PMGa39thoMMeWxp7Rp5oM8Q/",
            "https://drive.google.com/uc?export=download&id=1HIfDbVEWKmsYKJZm4lchTBDLW5N7dY5T"
            ]

        filenames = [os.path.basename(url).split("?")[0] for url in image_archives_urls]
        paths = [os.path.join(self.data_directory, filename) for filename in filenames]

        # Download image archives
        for url, path in zip(image_archives_urls, paths):

            facecctv_ai.download.Downloader(url, path).download()

        # Extract images
        subprocess.call(["7z", "x", paths[0], "-o" + self.data_directory])

        # Delete image archives
        for path in paths:

            os.remove(path)

    def _get_bounding_boxes(self):

        url = "https://drive.google.com/uc?export=download&id=1sAl2oml7hK6aZRdgRjqQJsjV5CEr7nl4"
        facecctv_ai.download.Downloader(url, self.bounding_boxes_path).download()

    def _get_image_paths(self, data_directory):

        image_paths = glob.glob(os.path.join(data_directory, "**/*.jpg"), recursive=True)
        image_paths = [os.path.abspath(path) for path in image_paths]
        return image_paths

    def _get_bounding_boxes_map(self, bounding_boxes_path):

        bounding_boxes_lines = facecctv_ai.utils.get_file_lines(bounding_boxes_path)[2:]
        bounding_boxes_map = {}

        for line in bounding_boxes_lines:

            tokens = line.split()

            filename = tokens[0]

            integer_tokens = [round(token) for token in tokens[1:]]
            bounding_box = facecctv_ai.geometry.get_bounding_box(*integer_tokens)

            bounding_boxes_map[filename] = bounding_box

        return bounding_boxes_map


class DataSubsetBuilder:
    """
    A helper class for DatasetBuilder
    """

    def __init__(self, directory, image_paths, bounding_boxes_map, splits):

        self.data_directory = directory
        self.image_paths = image_paths
        self.bounding_boxes_map = bounding_boxes_map
        self.splits = splits

    def build(self):

        shutil.rmtree(self.data_directory, ignore_errors=True)
        os.makedirs(self.data_directory, exist_ok=True)

        training_image_paths = self.image_paths[self.splits[0]:self.splits[1]]
        validation_image_paths = self.image_paths[self.splits[1]:self.splits[2]]
        test_image_paths = self.image_paths[self.splits[2]:self.splits[3]]

        splitted_image_paths = [training_image_paths, validation_image_paths, test_image_paths]

        prefixes = ["training_", "validation_", "test_"]

        images_list_file_names = [prefix + "image_paths.txt" for prefix in prefixes]
        images_list_file_paths = [os.path.join(self.data_directory, filename)
                                  for filename in images_list_file_names]

        # Create files with image paths
        for image_list_path, image_paths in zip(images_list_file_paths, splitted_image_paths):
            self._create_paths_file(image_list_path, image_paths)

        bounding_boxes_list_file_names = [prefix + "bounding_boxes_list.txt" for prefix in prefixes]
        bounding_boxes_list_file_paths = [os.path.join(self.data_directory, filename)
                                          for filename in bounding_boxes_list_file_names]

        # Create files with bounding boxes lists
        for bounding_box_list_path, image_paths in zip(bounding_boxes_list_file_paths, splitted_image_paths):
            self._create_bounding_boxes_file(bounding_box_list_path, image_paths, self.bounding_boxes_map)

    def _create_paths_file(self, file_path, image_paths):

        paths = [path + "\n" for path in image_paths]

        with open(file_path, "w") as file:

            file.writelines(paths)

    def _create_bounding_boxes_file(self, file_path, image_paths, bounding_boxes_map):

        image_paths = [os.path.basename(path) for path in image_paths]

        header = str(len(image_paths)) + "\nimage_id x_1 y_1 width height\n"

        with open(file_path, "w") as file:

            file.write(header)

            for image_path in image_paths:

                bounds = [round(value) for value in bounding_boxes_map[image_path].bounds]

                x = bounds[0]
                y = bounds[1]
                width = bounds[2] - bounds[0]
                height = bounds[3] - bounds[1]

                line = "{}\t{} {} {} {}\n".format(image_path, x, y, width, height)
                file.write(line)