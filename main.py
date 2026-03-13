import cv2 as cv
import numpy as np
import sys

img_p = 'imges/delete.png'
img = cv.imread(img_p)

def gauss(x, y, std):
    n1 = np.exp(-(x**2+y**2)/(2*(std**2)))
    n2 = 1/(2*np.pi*std**2)
    return n2*n1

def set_kern(dim, std):
    if(dim%2 != 1):
        raise ValueError("You number isn't skibidi enough")
    arr = np.zeros((dim, dim))
    c = dim//2
    for x in range(dim):
        for y in range(dim):
            arr[x][y] = gauss(x-c, y-c, std)
    arr /= arr.sum() #no idea what this does tbh
    return arr

def calc(pos, image, kern):
    x = pos[0], y = pos[1]
    image[x][y]

def scan(image, dim, std):
    kern = set_kern(dim, std)
    #this has to be a np array
    for x in range(image):
        for y in range(image[x]):
            calc()