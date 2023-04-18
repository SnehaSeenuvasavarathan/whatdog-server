# Import libraries
import os
import glob

import numpy as np
# import PIL
# from PIL import Image

# import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from flask import Flask, render_template, request
import requests as rq
from federated_functions import *

app = Flask(__name__)
global_model = load_model('model_20.h5')

dic = {0: 'Maltese_dog', 1: 'Rottweiler', 2: 'Pekinese', 3: 'Blenheim_spaniel', 4: 'Basset', 5: 'Japanese_spaniel', 6: 'Chihuahua', 7: 'Afghan_hound', 8: 'Beagle', 9: 'Doberman', 10: 'Papillon', 11: 'Shih_Tzu', 12: 'Rhodesian_ridgeback', 13: 'Golden_retriever', 14: 'Siberian_husky', 15: 'Toy_terrier', 16: 'Labrador_retriever', 17: 'German_shepherd', 18: 'Bloodhound', 19: 'Bluetick'}

def make_prediction(X):
    pred = global_model.predict(X)
    return dic[np.argmax(pred)]

def update_model(new_X, new_y):

    global_weights = global_model.get_weights()
    local_model = create_model()
    local_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
    local_model.summary()
    local_model.set_weights(global_weights)
    print('XY SHAPE', new_X.shape, new_y.shape)
    local_model.fit(new_X, new_y, epochs=8)

    scaling_factor = weight_scaling_factor(3614, 1) # 30/3000 = 1/100 = 0.01
    local_weights = local_model.get_weights()
    a = scale_model_weights(global_weights, 1-scaling_factor)
    b = scale_model_weights(local_weights, scaling_factor)
    avg_weights = sum_scaled_weights([a,b])
    global_model.set_weights(avg_weights)

    global_model.save('model_20-1.h5')

@app.route("/predict", methods=['POST', 'GET'])
def predict():
    print("HEHEHEHEHEHHEHE>>>>>>>")
    if request.method == 'GET':
        return 'Hola'
    img = request.files['image']
    img_path = "static/uploads/" + img.filename
    img.save(img_path)
    img = image.load_img(img_path, target_size=(200, 200))
    img = image.img_to_array(img)
    X = img.reshape(1, 200, 200, 3)
    return make_prediction(X)

@app.route("/update", methods=['POST'])
def update():
    print("GLLLLLAAAAEEEE>>>>>")
    img = request.files['image']
    label = request.form.get('label')
    print('LABEL IS ', label)
    new_y = convert_label(label)
    img_path = "static/uploads/" + img.filename
    img.save(img_path)
    img = image.load_img(img_path, target_size=(200, 200))
    img = image.img_to_array(img)
    new_X = img.reshape(1, 200, 200, 3)
    print("BEFORE UPDATE")
    update_model(new_X, new_y)
    print("AFTWR UPDATE")
    return "Success"

if __name__ =='__main__':
	app.run(debug=False, port=8888)