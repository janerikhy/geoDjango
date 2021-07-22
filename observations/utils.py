from django.urls.base import reverse
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import json
from iMap.settings import IMAGE_CLASSIFICATION_MODEL, IMAGE_CLASSIFICATION_LABELS
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


IMG_SIZE = 256


def predict_img(img_filepath):
    img = tf.keras.preprocessing.image.load_img(
        img_filepath, target_size=(IMG_SIZE, IMG_SIZE)
    )
    # img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    predictions = IMAGE_CLASSIFICATION_MODEL.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(IMAGE_CLASSIFICATION_LABELS[np.argmax(score)], 100 * np.max(score))
    )
    results = {}
    scores = list(score.numpy())
    for i in range(len(scores)):
        results[IMAGE_CLASSIFICATION_LABELS[i]] = str(scores[i])

    print(json.dumps(results))

    # Want to sort the results so that the items with the highest values end up first
    results = dict(
        sorted(results.items(), key=lambda item: item[1], reverse=True))

    print(f'Sorted results: {json.dumps(results)}')

    return (IMAGE_CLASSIFICATION_LABELS[np.argmax(score)], 100*np.max(score)), results
