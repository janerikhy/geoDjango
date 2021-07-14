import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from iMap.settings import BASE_DIR, STATICFILES_DIRS
import os
import json

"""
PLAN:

1. Don't know if we actually need a directory for it, but should probably have access to the images used to train the image classification model
2. Create a model which allows for uploading the different/improved ML models to the app
3. When the model is available, load the data into this .py file and create related functionality

What we want to achieve:

When the user uploads an image, the image should be stored as an observation with extraction of the different interesting attributes (point, timestamp etc).

The model can be loaded by accessing the model directory as:
        new_model = tf.keras.models.load_model(model_dir_path)

The directory contains: assets, keras_metadata.pb save_model.pb and variables

Currently the model is stored in the static files directory.

Before we can predict what the image has stored we must perform some preprocessing of the image.
"""

MODEL_DIR = os.path.join(
    STATICFILES_DIRS[0], 'models', 'ML_MODEL', 'first_model')

model = tf.keras.models.load_model(MODEL_DIR)

json_file = open(os.path.join(MODEL_DIR, 'classes.json'))
classes = json.load(json_file)
json_file.close()

class_names = list(classes.values())[0]

IMG_SIZE = 256


def predict_img(img_filepath):
    img = tf.keras.preprocessing.image.load_img(
        img_filepath, target_size=(IMG_SIZE, IMG_SIZE)
    )
    # img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score)], 100 * np.max(score))
    )
