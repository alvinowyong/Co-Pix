# import time

# from tensorflow.keras import Sequential
from tensorflow.keras.models import load_model
# import cv2
# import numpy as np
# from tensorflow.keras.preprocessing.image import img_to_array


 # Load the model
# model = Sequential()
classifier = load_model('model_fer.h5') # This model has a set of 6 classes
print(classifier.summary())