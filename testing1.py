#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lab 1: Introduction to Python and One-Dimensional (1-D) Convolution

Created on Tue Jan  4 20:10:07 2022

@author: etharhussein
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------- PART A --------------------
### PART 1
# create a vector
x = np.array([0.,0.,1.,1.,1.,1.,1.,1.,1.,1.])
print(x)

# now display the vector
fig1 = plt.figure(1)
plt.stem(x)
plt.pause(1) 
# flush the plot out. pauses fro 1 second. without the pause, it won't show thethe firgiure until the end.
# ????? - why not plt.pause(0.0001)
''' This will be u[n], d is 1. '''


# create vector of range -2:7
k = np.arange(-2.,8.,1.)

fig2 = plt.figure(2)
plt.stem(k,x)
plt.show()
''' This is u[n-d], d = 2. '''

# ---------------------------
### PART 2
k =  np.arange(-10.,20.+1.,1.)
x = np.hstack([np.zeros(shape=(10)), np.ones(shape=(20+1))])

fig2 = plt.figure(3)
plt.stem(k,x)
plt.show()
''' This is u[n] for -10 <= n <= 20. '''


k = np.arange(-15,16,1.) #np.arange(-10.-5,20.+1-5,1.)
fig4 = plt.figure(4)
plt.stem(k,x)
plt.show()
''' This is u[n-5] for -10 <= n <= 20 '''

# ---------------------------
### PART 3
# np.cos() function
k = np.arange(-40,81,1) # -40 <= k <= 80
x = 7*np.cos(0.1*k)+np.cos(0.95*k) # x[n]=7cos(0.1n)+cos(0.95n)

fig5 = plt.figure(5)
plt.stem(k,x)
plt.show()
""" This is for u[n]. This is 
x[n]=7cos(0.1n)+cos(0.95n) for -40 <= n <= 80. 
k is n in this case.  """

# now this will be for n-20
k = np.arange(-60,61,1)
x = 7*np.cos(0.1*k)+np.cos(0.95*k) # need to re-evaluate for new k
fig6 = plt.figure(6)
plt.stem(k,x)
plt.show()
''' This is x[n-20] for -40 <= n <= 80 '''


#----------- PART B ----------------
# 1 - D Convoltuion
# PART 1
# PART 2

h = 1./5.*np.array([1.,1.,1.,1.,1.])

# A. 
k = np.arange(0,21,1)
x = np.ones(shape=len(k))
y = np.convolve(x,h)
fig1 = plt.figure(1)
plt.stem(y)
plt.show()

# B.
k = np.arange(-40,81,1)
x = np.cos(0.1*k)
y = np.convolve(x,h)
fig2 = plt.figure(2)
plt.stem(y)
plt.show()

# C. 
k = np.arange(-40,81,1)
x = np.cos(0.95*k)
y = np.convolve(x,h)
fig3 = plt.figure(3)
plt.stem(y)
plt.show()

# D.
k = np.arange(-40,81,1)
x = 7*np.cos(0.1*k)+np.cos(0.95*k) # form part A number 3
y = np.convolve(x,h)
fig4 = plt.figure(4)
plt.stem(y)
plt.show()

#---------------------------
# PART 3 - just like part 2, but h is different
h=[1,-1]

# A.
k = np.arange(0,21,1)
x = np.ones(shape=len(k))
y = np.convolve(x,h)
fig5 = plt.figure(5)
plt.stem(y)
plt.show()

# B.
k = np.arange(-40,81,1)
x = np.cos(0.1*k)
y = np.convolve(x,h)
fig6 = plt.figure(6)
plt.stem(y)
plt.show()

# C. 
k = np.arange(-40,81,1)
x = np.cos(0.95*k)
y = np.convolve(x,h)
fig7 = plt.figure(7)
plt.stem(y)
plt.show()

# D.
k = np.arange(-40,81,1)
x = 7*np.cos(0.1*k)+np.cos(0.95*k) # form part A number 3
y = np.convolve(x,h)
fig8 = plt.figure(8)
plt.stem(y)
plt.show()

#---------------------------
# PART 4
''' Accoridng to step 2 and 3, the average 
system smoothed out the signal and reduced 
the difference between subsequent points in 
most cases.

The difference system is led to destructive
interference and squished the signals.'''













