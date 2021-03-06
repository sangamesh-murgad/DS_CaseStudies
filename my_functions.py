# -*- coding: utf-8 -*-
"""My_functions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y4NMnZYh4KQzGmxzJnqqborgpfJ6tI45
"""

import datetime
import tensorflow as tf

# Create a tensorboard call back function
def create_tensorboard_callback(dir_name,experiment_name):
  log_dir = dir_name + '/' + experiment_name + '/' + datetime.datetime.now().strftime("%y%m%d-%H%M%S")
  tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir = log_dir)
  print(f'saving tensorboard log files to "{log_dir}".')
  return tensorboard_callback

# Create a Plot loss curves function

import matplotlib.pyplot as plt

def plot_loss_curves(history):
  """
  Returns separate loss curves for training and validation metrics / loss

  Args:
  - history: Tensorflow history object

  Retruns:
  - Plots for Loss and accuracy for training and validation separately
  """

  loss = history.history['loss']
  val_loss = history.history['val_loss']

  accuracy = history.history['accuracy']
  val_accuracy = history.history['val_accuracy']

  epochs = range(len(history.history['loss']))

  #plot curves
  plt.figure(figsize = (15,6))
  # plt.subplots(1,2,1)
  plt.plot(epochs,loss,label = 'Training loss')
  plt.plot(epochs,val_loss, label = 'Validation loss')
  plt.title('Training vs Validation loss curves')
  plt.legend()
  plt.xlabel('epochs')

  plt.figure(figsize = (15,6))
  # plt.subplots(1,2,2)
  plt.plot(epochs, accuracy, label = 'Training accuracy')
  plt.plot(epochs, val_accuracy, label = 'Validation accuracy')
  plt.title('Training vs Validation Accuracy curves')
  plt.xlabel('epochs')
  plt.legend()

## Make a function to predict on images and plot them (works with multi-class)
def pred_and_plot(model, filename, class_names):
  """
  Imports an image located at filename, makes a prediction on it with
  a trained model and plots the image with the predicted class as the title.
  """
  # Import the target image and preprocess it
  img = load_and_prep_image(filename)

  # Make a prediction
  pred = model.predict(tf.expand_dims(img, axis=0))

  # Get the predicted class
  if len(pred[0]) > 1: # check for multi-class
    pred_class = class_names[pred.argmax()] # if more than one output, take the max
  else:
    pred_class = class_names[int(tf.round(pred)[0][0])] # if only one output, round

  # Plot the image and predicted class
  plt.imshow(img)
  plt.title(f"Prediction: {pred_class}")
  plt.axis(False);

# Create a function to unzip the data from a zip folder
import zipfile

def unzip_data(filename):
  """
  Unzips filename into the current working directory.

  Args:
    filename (str): a filepath to a target zip folder to be unzipped.
  """
  zip_ref = zipfile.ZipFile(filename, "r")
  zip_ref.extractall()
  zip_ref.close()

# Walk through an image classification directory and find out how many files (images)
# are in each subdirectory.
import os

def walk_through_dir(dir_path):
  """
  Walks through dir_path returning its contents.

  Args:
    dir_path (str): target directory
  
  Returns:
    A print out of:
      number of subdiretories in dir_path
      number of images (files) in each subdirectory
      name of each subdirectory
  """
  for dirpath, dirnames, filenames in os.walk(dir_path):
    print(f"There are {len(dirnames)} directories and {len(filenames)} images in '{dirpath}'.")