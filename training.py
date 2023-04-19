import os
import glob
import tensorflow as tf
from PIL import Image
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from sklearn.model_selection import train_test_split
import numpy as np

def create_model_new_class(num_classes):
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
    model.add(tf.keras.layers.Dense(num_classes, activation='softmax'))
    return model

def train(model, X, Y):
    model.fit(X, Y, epochs = 2, batch_size = 10)
    model.save('model_20-2.h5')

def load_data():
    # Load the dataset
    path = 'data/'
    count = []
    folders = ([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]) # get all directories
    num_classes = len(folders)
    for folder in folders:
        contents = os.listdir(os.path.join(path,folder)) # get list of contents
        count.append(len(contents))
    s = sum(count)
    newsize = (200, 200)
    X=np.zeros((s,200,200,3))
    files = glob.glob('data/**/*.jpg', recursive=True)
    labels=[]
    for i,filename in enumerate(files):
        with Image.open(filename) as im:
            im = im.resize(newsize)
            a=np.array(im)
            if a.shape[2]>3:
                print(filename)
                continue
            X[i]=a
    
    # Load labels
    Y = np.zeros((s, num_classes))
    v=0
    for i in range(num_classes):
        for j in range(count[i]):
            Y[v,i]=1.0
            v+=1
    return X, Y, num_classes

