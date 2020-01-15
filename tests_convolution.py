from PIL import Image
import matplotlib.pyplot as plt
import imageUtils as imgutil
import convolution
import numpy as np

img = Image.open('linia.png').convert('L')
binimg = imgutil.binarize(img,128)
#mask = np.matrix([[1, 2, 1],[2,4,2],[1,2,1]], dtype=np.uint8)
mask = np.matrix([[1, 2, 4, 2, 1],[2,4, 8, 4 ,2],[1,2, 4, 2,1]], dtype=np.uint8)
convimg = convolution.convolve(binimg,mask)
imgplot = imgutil.imshow_gray(imgutil.invert(convimg))
plt.show()
