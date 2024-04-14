import pandas as pd
import cv2 as cv
import numpy as np 
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt

import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

import torch

print(f'\nAvailable cuda = {torch.cuda.is_available()}')

print(f'\nGPUs availables = {torch.cuda.device_count()}')

print(f'\nCurrent device = {torch.cuda.current_device()}')

print(f'\nCurrent Device location = {torch.cuda.device(0)}')

print(f'\nName of the device = {torch.cuda.get_device_name(0)}')