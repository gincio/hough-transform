import matplotlib.pyplot as plt
import numpy as np

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def imshow_gray(img):
    return plt.imshow(img, cmap='gray', vmin=0, vmax=255)

def binarize(img,th):
    return (np.asarray(img) > th) * 255

def invert(img):
    return abs(np.asarray(img) - 255)


