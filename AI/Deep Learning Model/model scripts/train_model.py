import os

import keras

import face.config
import face.data_generator
import face.models
import face.utils

def get_callbacks():

      model_path = face.config.model_path
      os.makedirs(os.path.dirname(model_path), exist_ok=True)
      model_save_checkpoint = keras.callbacks.ModelCheckpoint(filepath=model_path, save_best_only=True, verbose=1)

      reduce_learning_rate = keras.callbacks.ReduceLROnPlateau(factor=0.7, patience=2, verbose=1)
      early_stop_callbacks = keras.callbacks.EarlyStopping(patience=8, verbose=1)

      return [model_save_checkpoint, reduce_learning_rate, early_stop_callbacks]

def main():
      # dataset = "custom_dataset"
      dataset = "wider_face_dataset"

      dataset_path = os.path.join(face.config.dataset_path, dataset)

      training_image_path_file = face.utils.join(dataset_path, "training_images.txt")
      training_bounding_box_file = face.utils.join(dataset_path, "training_bounding_boxes.txt")

      validation_image_path_file = face.utils.join(dataset_path, "validation_images.txt")
      validation_bounding_box_file = face.utils.join(dataset_path, "validation_bounding_boxes.txt")

      batch_size = face.config.batch_size

      model = face.models.get_vgg_model(image_shape=face.config.image_shape)

      training_data_generator = face.data_generator.get_data_batch_generator(training_image_path_file, training_bounding_box_file, batch_size, face.config.crop_size)
      validation_data_generator = face.data_generator.get_data_batch_generator(validation_image_path_file, validation_bounding_box_file, batch_size, face.config.crop_size)

      model.fit_generator(
            training_data_generator, samples_per_epoch=face.utils.get_file_line_count(training_image_path_file), epochs=100, validation_data=validation_data_generator, val_samples=face.utils.get_file_line_count(validation_image_path_file), callbacks=get_callbacks()
      )

if __name__ == "__main__":
      main()