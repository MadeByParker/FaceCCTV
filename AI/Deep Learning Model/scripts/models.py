import keras
import keras.applications

def get_vgg_model(image_shape):
      expected_input_shape = (64, 64, 3)

      if image_shape != expected_input_shape:
            message = "Input image is specified as {}, but the model is designed to work with inputs of shape {}"\
                  .format(image_shape, expected_input_shape)

            raise ValueError(message)
      
      input_layer = keras.layers.Input(shape=image_shape)

      x = keras.applications.VGG16(include_top=False, weights='imagnet')(input_layer)
      x = keras.layers.Convolution2D(1, 2, 2, activation='sigmoid', name="final_convolution")(x)
      x = keras.layers.Flatten()(x)

      model = keras.models.Model(input=input_layer, output=x)

      adam = keras.optimizers.Adam(lr=0.0001)
      
      model.compile(optimizer=adam, loss="binary_crossentropy", metrics=["accuracy"])

      return model

def get_medium_scale_model(image_shape):
      expected_input_shape = (100, 100, 3)

      if image_shape != expected_input_shape:
            message = "Input image is specified as {}, but the model is designed to work with inputs of shape {}"\
                  .format(image_shape, expected_input_shape)

            raise ValueError(message)

      input_layer = keras.layers.Input(shape=image_shape)

      # Block 1
      x = keras.layers.Convolution2D(64, 3, 3, activation='elu', border_mode='same', name='block1_conv1')(input_layer)
      x = keras.layers.Convolution2D(64, 3, 3, activation='elu', border_mode='same', name='block1_conv2')(x)
      x = keras.layers.MaxPooling2D((2, 2), strides=(2, 2), name='block1_pool')(x)

      # Block 2
      x = keras.layers.Convolution2D(128, 3, 3, activation='elu', border_mode='same', name='block2_conv1')(x)
      x = keras.layers.Convolution2D(128, 3, 3, activation='elu', border_mode='same', name='block2_conv2')(x)
      x = keras.layers.MaxPooling2D((2, 2), strides=(2, 2), name='block2_pool')(x)

      # Block 3
      x = keras.layers.Convolution2D(256, 3, 3, activation='elu', border_mode='same', name='block3_conv1')(x)
      x = keras.layers.Convolution2D(256, 3, 3, activation='elu', border_mode='same', name='block3_conv2')(x)
      x = keras.layers.Convolution2D(256, 3, 3, activation='elu', border_mode='same', name='block3_conv3')(x)
      x = keras.layers.MaxPooling2D((2, 2), strides=(2, 2), name='block3_pool')(x)

      # Block 4
      x = keras.layers.Convolution2D(512, 3, 3, activation='elu', border_mode='same', name='block4_conv1')(x)
      x = keras.layers.Convolution2D(512, 3, 3, activation='elu', border_mode='same', name='block4_conv2')(x)
      x = keras.layers.Convolution2D(512, 3, 3, activation='elu', border_mode='same', name='block4_conv3')(x)
      x = keras.layers.MaxPooling2D((2, 2), strides=(2, 2), name='block4_pool')(x)

      x = keras.layers.Convolution2D(1, 6, 6, activation='sigmoid', name="final_convolution")(x)
      x = keras.layers.Flatten()(x)

      model = keras.models.Model(input=input_layer, output=x)

      adam = keras.optimizers.Adam(lr=0.000001)
      model.compile(optimizer=adam, loss="binary_crossentropy", metrics=["accuracy"])

      return model