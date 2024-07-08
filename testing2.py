#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lab 2: Basic Image Processing Using Python

Created on Tue Jan  4 20:22:54 2022

@author: etharhussein
"""

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# cv.read read the image from disk to numpy array
img = cv.imread("boat.jpeg", cv.IMREAD_GRAYSCALE) 

# size of the image
print("Intro - The Image Shape:",img.shape)

# display image to screen
plt.imshow(img, cmap='gray')
plt.show()

'''But first we need to convert 
the image from type “uint8” into”float32”
 and normalize it by 255. '''

img = img.astype(np.float32)/255.

# display image to make sure its the same as above and correct
plt.imshow(img, cmap='gray')
plt.show()

#----------------------------
# Number 1
# Printing the value of the pixel at location (132,112)
print('Number 1:', img[132,112])
#----------------------------
# Number 2
# Displaying the top-left quarter of the image (with 2-D slicing: x[a:b,a:b])
# ????????????????????????????
# do img.shape for the size 500 * 500 .t he 1st quarter is 125*125. top left is 0,0. bottm right will be the largest number
plt.imshow(img[0:384, 0:384],cmap='gray') #how did you know the slicing?
plt.show()
#----------------------------
# Number 3
# implement linear filtering
ma = 1./9.*np.array([[1.,1.,1.,],[1.,1.,1.],[1.,1.,1.,]])

# perform two-dimensional (2-D) convolution.
# convolve the image with the moving average filter “ma”
from scipy.signal import convolve2d
img_filtered = convolve2d(img, ma)

# size of the filtered  image
print(img.shape)
print(img_filtered.shape)

# display filtrered imaged
plt.imshow(img_filtered, cmap='gray')
plt.show()

# PRINT HERE THE DIFF !!!!!!
#----------------------------
# Number 4
# save the image to computer
# grayscale images are from 0 to 1
img_filtered = img_filtered * 255
cv.imwrite("boat_filtered.jpeg", img_filtered)

'''look up on computer and make sure it looks like
the image you displayed on your computer '''

#----------------------------
# Number 5
# now we make 3-by-3 difference filter
# first row:[1,0,-1], second row: [2,0,-2], third row:[1,0,-1]).
df = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
print("Number 5:\n", df)

#display with the filter with convolve2d
img_diff = convolve2d(img,df) + 0.5 # need to add 0.5 to output pixels
print("Number 5:", img_diff.shape)
plt.imshow(img_diff,cmap='gray')
plt.show()
'''img_diff is size 770x770. The img_diff 
shows the details or edges of img.'''
#??????? 
# i got differnet answers. shouldn't the coment 
# be (2138, 3202) not 770x770 when you run the program?

#----------------------------
# Number 6

# Detecting horizontal edges of the image
# using the filter [-1 2 -1].
# just like 5
horizontal = np.array([[-1, 2,-1]])
img_horiz = convolve2d(img,horizontal) + 0.5
plt.imshow(img_horiz,cmap='gray')
plt.show()

#----------------------------
# Number 7

# Detecting vertical edges of the image
# using the filter [-1 2 -1].
# just like 6
vertical = np.array([[-1],[2], [-1]]) # this is how you do vertical
img_horiz = convolve2d(img,horizontal) + 0.5
plt.imshow(img_horiz,cmap='gray')
plt.show()

#----------------------------
# Number 8
# same experiements but with colorful picture
'''opencv, imwrite,imread is normally BGR format. so you have
to covnert with back to RGB format when you want to channel a lot of colors. '''

img2 = cv.imread("pink_room.jpeg")
img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)

#----------------------------
# Number 1.2
print("Number 1.2:",img2.shape)
plt.imshow(img2)
plt.show()

#----------------------------
# Number 2.2
img2 = img2.astype(np.float32)/255
print(img2[132,112])

plt.imshow(img2[0:384, 0:384])
plt.show()

#----------------------------
# Number 3.2
red = img2[:,:,0]
red_filtered = convolve2d(red, ma)
green = img2[:,:,1]
green_filtered = convolve2d(green, ma)
blue = img2[:,:,2]
blue_filtered = convolve2d(blue, ma)

img2_filtered = np.dstack((red_filtered,green_filtered,blue_filtered))
print(img2_filtered.shape)
plt.imshow(img2_filtered)
plt.show()
# img2_filtered is size 770x770x3
# img2_filtered is blurrier than img2 and the colors are less saturated

#----------------------------
# Number 4.2
img2_filtered = np.dstack((blue_filtered,green_filtered,red_filtered)) * 255
cv.imwrite('pink_room_filtered.jpeg',img2_filtered)

#----------------------------
# Number 5.2

red_diff = convolve2d(red, df)
green_diff = convolve2d(green, df)
blue_diff = convolve2d(blue, df)

img2_diff = np.dstack((red_diff,green_diff,blue_diff))
print(img2_diff.shape)
plt.imshow(img2_diff)
plt.show()
# img_diff is size 770x770x3
# img_diff shows the lines of the image, like a negative version of it

#----------------------------
# Number 6.1
red_hori = convolve2d(red, horizontal)
green_hori = convolve2d(green, horizontal)
blue_hori = convolve2d(blue, horizontal)

img2_horizontal = np.dstack((red_hori,green_hori,blue_hori))
plt.imshow(img2_horizontal)
plt.show()

#----------------------------
# Number 7.2
red_vert = convolve2d(red, vertical)
green_vert = convolve2d(green, vertical)
blue_vert = convolve2d(blue, vertical)

img2_vertical = np.dstack((red_vert,green_vert,blue_vert))
plt.imshow(img2_vertical)
plt.show()

# ???????????????
# what do they mean by clipping?
# and it didnt the pink_room_filter saved pic is prob not right







