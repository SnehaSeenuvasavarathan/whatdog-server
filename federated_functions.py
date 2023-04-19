import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D
import numpy as np

def convert_label(label, no_of_files):
    dct = {'Maltese_dog': 0, 'Rottweiler': 1, 'Pekinese': 2, 'Blenheim_spaniel': 3, 'Basset': 4, 'Japanese_spaniel': 5, 'Chihuahua': 6, 'Afghan_hound': 7, 'Beagle': 8, 'Doberman': 9, 'Papillon': 10, 'Shih_Tzu': 11, 'Rhodesian_ridgeback': 12, 'Golden_retriever': 13, 'Siberian_husky': 14, 'Toy_terrier': 15, 'Labrador_retriever': 16, 'German_shepherd': 17, 'Bloodhound': 18, 'Bluetick': 19}
    y = np.zeros((no_of_files,20))
    for i in range(no_of_files):
        y[i, dct[label]] = 1
    print(y)
    return y

def create_model():
    model=Sequential()
    model.add(Conv2D(16, ( 3, 3), padding='same', activation='relu', input_shape=(200, 200, 3)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(32, ( 3, 3), padding='same', activation='relu', input_shape=(200, 200, 16)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), padding='same', activation='relu', input_shape=(200, 200, 32)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(128, (3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(20, activation='softmax'))
    return model

def weight_scaling_factor(data, new_data):
    return new_data/data

def scale_model_weights(weight, scalar):
    '''function for scaling a models weights'''
    weight_final = []
    steps = len(weight)
    for i in range(steps):
        weight_final.append(scalar * weight[i])
    return weight_final
def sum_scaled_weights(scaled_weight_list):
    '''Return the sum of the listed scaled weights. The is equivalent to scaled avg of the weights'''
    avg_grad = list()
    #get the average grad accross all client gradients
    for grad_list_tuple in zip(*scaled_weight_list):
        layer_mean = tf.math.reduce_sum(grad_list_tuple, axis=0)
        avg_grad.append(layer_mean)
        
    return avg_grad
