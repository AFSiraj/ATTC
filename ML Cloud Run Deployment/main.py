from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Sequential, load_model
from flask import Flask, request, flash, redirect
from PIL import Image
import flask
import numpy as np
import pandas as pd
import tensorflow as tf
import io

# from keras.models import load_model

# instantiate flask
app = Flask(__name__)

#  load model, and pass in the custom metric
global graph
graph = tf.compat.v1.get_default_graph()
model = load_model('traditional_cake.h5')


def prepare_image(image, target_size):
    # resize the input image and preprocess it
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = np.vstack([image])

    # return the processed image
    return image


class_names = ['kue_dadar_gulung', 'kue_kastengel', 'kue_klepon',
               'kue_lapis', 'kue_lumpur', 'kue_putri_salju', 'kue_risoles', 'kue_serabi']


@app.route("/")
def hello():
    return "Hello, Bangkit!"


@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}

    if flask.request.method == "POST":
        # check if the post has "image" file part
        if 'image' not in request.files:
            data['message'] = "No image part"
            return flask.jsonify(data), 404

        file = request.files['image']

        if file.filename == '':
            data['message'] = "No selected image"
            return flask.jsonify(data), 404

        if file:
            # read the image in PIL format
            image = file.read()
            image = Image.open(io.BytesIO(image))

            data["filename"] = file.filename

            # preprocess the image and prepare it for classification
            resizedImage = prepare_image(image, target_size=(150, 150))

            classes = model.predict(resizedImage, batch_size=10)

            x = np.where(classes[0] == 1)[0][0]

            data["prediction"] = class_names[x]
            data["x_value"] = str(classes)

            # 0,2,4,7  https://storage.googleapis.com/attc-bucket/packaging/mica_green.jpg
            # 1,5 https://storage.googleapis.com/attc-bucket/packaging/mica_toples.jpg
            # 3 https://storage.googleapis.com/attc-bucket/packaging/cake_box.jpg
            # 6 https://storage.googleapis.com/attc-bucket/packaging/paperkraft_box.jpg
            if x == 0 or x == 2 or x == 4 or x == 7:
                data["packaging_url"] = "https://storage.googleapis.com/attc-bucket/packaging/mica_green.jpg"
                data["packaging_name"] = "Plastik Mica"

            if x == 1 or x == 5:
                data["packaging_url"] = "https://storage.googleapis.com/attc-bucket/packaging/mica_toples.jpg"
                data["packaging_name"] = "Toples Mica"

            if x == 3:
                data["packaging_url"] = "https://storage.googleapis.com/attc-bucket/packaging/cake_box.jpg"
                data["packaging_name"] = "Cake Box"

            if x == 6:
                data["packaging_url"] = "https://storage.googleapis.com/attc-bucket/packaging/paperkraft_box.jpg"
                data["packaging_name"] = "Box Paperkraft"

            # indicate that the request was a success
            data["success"] = True

    print("data: {}".format(data))
    print("data_type: {}".format(type(data)))

    return flask.jsonify(data)


@app.route("/coba", methods=["POST"])
def coba():
    data = {"success": False}

    if flask.request.method == "POST":
        # check if the post has "image" file part
        if 'image' not in request.files:
            data['message'] = "No image part"
            return flask.jsonify(data), 404

        file = request.files['image']

        if file.filename == '':
            data['message'] = "No selected image"
            return flask.jsonify(data), 404

        if file:
            # read the image in PIL format
            image = file.read()
            image = Image.open(io.BytesIO(image))

            data["filename"] = file.filename

            # preprocess the image and prepare it for classification
            resizedImage = prepare_image(image, target_size=(150, 150))

            classes = model.predict(resizedImage, batch_size=10)

            x = np.where(classes[0] == 1)[0][0]

            data["prediction"] = class_names[x]
            data["x_value"] = str(classes)

            # indicate that the request was a success
            data["success"] = True

    print("data: {}".format(data))
    print("data_type: {}".format(type(data)))

    return flask.jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
