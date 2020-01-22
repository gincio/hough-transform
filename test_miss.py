from PIL import Image
import matplotlib.pyplot as plt
import imageUtils as imgutil
import numpy as np
import imageProcessor as ip

img1 = Image.open('line_test_2.jpg').convert('L')
img2 = Image.open('line_test_1.jpg').convert('L')
binimg1 = imgutil.binarize(img1,195)
binimg2 = imgutil.binarize(img2,195)
#imgutil.imshow_gray(binimg1)
#plt.show()
miss = ip.calculateMiss(binimg1,binimg2)
print(str(miss))
