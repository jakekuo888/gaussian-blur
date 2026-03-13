# REALLY [HYPERLINK_BLOCKED] SLOW VERSION.
import cv2 as cv
import numpy as np
import sys

img_p = 'imges/delete.png'
img = cv.imread(img_p, cv.IMREAD_GRAYSCALE)

def gauss(x, y, std):
    n1 = np.exp(-(x**2+y**2)/(2*(std**2)))
    n2 = 1/(2*np.pi*std**2)
    return n2*n1

def set_kern(dim, std):
    if(dim%2 != 1):
        raise ValueError("Dims aren't skibidi enough")
    arr = np.zeros((dim, dim))
    c = dim//2
    for x in range(dim):
        for y in range(dim):
            arr[x][y] = gauss(x-c, y-c, std)
    arr /= arr.sum()
    return arr

def calc(x, y, image, kern, dim):
    img_x = len(image) #x
    img_y = len(image[0]) #y
    imgdata = np.zeros((dim, dim))
    d2 = dim//2
    for i in range(dim):
        for j in range(dim):
            img_i = x+i-d2
            img_j = y+j-d2

            img_i = min(max(img_i, 0), img_x-1)
            img_j = min(max(img_j, 0), img_y-1)

            imgdata[i][j] = image[img_i][img_j]
    
    return np.sum(imgdata * kern)

def scan(image, dim, std):
    kern = set_kern(dim, std)
    g_img = np.zeros((len(image), len(image[0])), dtype=np.uint8)
    #this has to be a np array
    for x in range(len(image)):
        for y in range(len(image[0])):
            g_img[x][y] = calc(x, y, image, kern, dim)
    return g_img

g_img = scan(img, 15, 3)
cv.imwrite('imges/out.png', g_img)