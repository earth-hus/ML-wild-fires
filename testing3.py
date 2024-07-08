#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 16:38:57 2022

Lab 3: MNIST Digit Recognition Using a Perceptron

@author: etharhussein
"""
#----------------------------
# Number 1,2,3,4
import gzip
import os
import struct
import numpy as np
import matplotlib.pyplot as plt

DATASET_DIR = "dataset"
MNIST_TRAIN_IMS_GZ = os.path.join(DATASET_DIR, "train-images-idx3-ubyte.gz")
MNIST_TRAIN_LBS_GZ = os.path.join(DATASET_DIR, "train-labels-idx1-ubyte.gz")
MNIST_TEST_IMS_GZ = os.path.join(DATASET_DIR, "t10k-images-idx3-ubyte.gz")
MNIST_TEST_LBS_GZ = os.path.join(DATASET_DIR, "t10k-labels-idx1-ubyte.gz")
NROWS = 28
NCOLS = 28


#----------------------------
# Number 5
def load_data():
    print("Unpacking training images ...")
    with gzip.open(MNIST_TRAIN_IMS_GZ, mode='rb') as f:
        magic_num, train_sz, nrows, ncols = struct.unpack('>llll', f.read(16))
    print("magic number: %d, num of examples: %d, rows: %d, columns: %d" %
    (magic_num, train_sz, nrows, ncols))
    data_bn = f.read()
    data = struct.unpack('<'+'B'*train_sz*nrows*ncols, data_bn)
    train_ims = np.asarray(data)
    train_ims = train_ims.reshape(train_sz, nrows*ncols)
    print("~"*5)
    print("Unpacking training labels ...")
    with gzip.open(MNIST_TRAIN_LBS_GZ, mode='rb') as f:
        magic_num, train_sz = struct.unpack('>ll', f.read(8))
    print("magic number: %d, num of examples: %d" % (magic_num, train_sz))
    data_bn = f.read()
    data = struct.unpack('<'+'B'*train_sz, data_bn)
    train_lbs = np.asarray(data)
    print("~"*5)
    print("Unpacking test images ...")
    with gzip.open(MNIST_TEST_IMS_GZ, mode='rb') as f:
        magic_num, test_sz, nrows, ncols = struct.unpack('>llll', f.read(16))
    print("magic number: %d, num of examples: %d, rows: %d, columns: %d" %
    (magic_num, train_sz, nrows, ncols))
    data_bn = f.read()
    data = struct.unpack('<'+'B'*test_sz*nrows*ncols, data_bn)
    test_ims = np.asarray(data)
    test_ims = test_ims.reshape(test_sz, nrows*ncols)
    print("~"*5)
    
    print("Unpacking test labels ...")
    with gzip.open(MNIST_TEST_LBS_GZ, mode='rb') as f:
        magic_num, test_sz = struct.unpack('>ll', f.read(8))
    print("magic number: %d, num of examples: %d" % (magic_num, train_sz))
    data_bn = f.read()
    data = struct.unpack('<'+'B'*test_sz, data_bn)
    test_lbs = np.asarray(data)
    print("~"*5)
    return train_ims, train_lbs, test_ims, test_lbs

train_ims, train_lbs, test_ims, test_lbs = load_data()

""" As we have 60,000 images in the training dataset, 
“train_ims” will be a 2d numpy array of size 60,000-by-784,
 where 60,000 is the number of examples, 784 is the size of 
 the image (NROWS-by-NCOLS)."""
 
 #----------------------------
 # Question 1
 # Print out the shapes of the 4 numpy array
 
print(train_ims.shape)
print(train_lbs.shape)
print(test_ims.shape)
print(test_lbs.shape)
print('-'*5)


#----------------------------
# Question 2
# display the images on the screen
# like lab 2
''' “train_ims” is the 5th image vectorized,
s# o you need to reshape it into a 28-by-28 image
in order to display it on screen.'''

plt.imshow(np.reshape(train_ims[4,:], (28,28)),cmap='gray')
plt.show()
print(train_lbs[4])
print('-'*5)

#----------------------------
# Question 3
# Repeat Q1 and Q2 for the test data (“test_ims” and “test_lbs”).
plt.imshow(np.reshape(test_ims[4,:], (28,28)),cmap='gray')
plt.show()
print(test_lbs[4])
print('-'*5)


#----------------------------
# Question 4
# Now we need only the examples of class “0” and “1”. 
# We need to do logical indexing over the data set.
mask = np.logical_or(train_lbs==0, train_lbs==1)
train_ims = train_ims[mask,:]
train_lbs = train_lbs[mask]
print(train_ims.shape)
print(train_lbs.shape)

print("Question 4.2: after filterung, there is 12665 examples")
print('-'*5)
#----------------------------
# Question 5
# Repeat Q4 for the test data. 
mask = np.logical_or(test_lbs==0, test_lbs==1)
test_ims = test_ims[mask,:]
test_lbs = test_lbs[mask]
print(test_ims.shape)
print(test_lbs.shape)
print("Question 5.2: after filterung, there is 2115 examples")
print('-'*5)
#----------------------------
# Question 6
'''Now extract a validation data set. You can obtain 
your validation data set by taking the last 20% of the training dataset'''
val_ims = train_ims[:int(0.8*train_ims.shape[0]),:]
train_ims = train_ims[int(0.8*train_ims.shape[0]):,:]
print(val_ims.shape)
print(train_ims.shape)

val_lbs = train_lbs[:int(0.8*train_lbs.shape[0])]
train_lbs = train_lbs[int(0.8*train_lbs.shape[0]):]
print(val_lbs.shape)
print(train_lbs.shape)

print("Question 6.2: There are 2533 validation ")
print("samples and 10132 training samples")
print('-'*5)

#----------------------------
# Question 7
# TYPE-CAST all the the numpy arrays (images arrays and labels vectors) 
# from “uint8” type to “float32”.
train_ims = train_ims.astype(np.float32)
val_ims = val_ims.astype(np.float32)
test_ims = test_ims.astype(np.float32)

train_lbs = train_lbs.astype(np.float32)
val_lbs = val_lbs.astype(np.float32)
test_lbs = test_lbs.astype(np.float32)




