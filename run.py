from PIL import Image
import matplotlib.pyplot as plt
import imageUtils as imgutil
from houghSpace import HoughSpace
import math
import numpy as np
import drawer as dr
import sys

imgName = sys.argv[1]
img = Image.open(imgName).convert('L')
binimg = imgutil.binarize(img,128)

#plt.show()

hough = HoughSpace(binimg)
maxPos = hough.getMaxPosition()
r = hough.getRadius(maxPos)
th = -1.0 * hough.getAngle(maxPos)
[a,b] = hough.getLineParams()
hough.showHoughSpace()

mask = np.matrix([[1, 2, 1],[2,4,2],[1,2,1]], dtype=np.uint8)
hough.convolveHoughSpace(mask)
maxPos = hough.getMaxPosition()
r = hough.getRadius(maxPos)
th = -1.0 * hough.getAngle(maxPos)
[a,b] = hough.getLineParams()
hough.showHoughSpace()
#line = dr.calculateline(a,b,500,500)
plt.figure('linia')
dr.drawline(r,th)
#imgplot = imgutil.imshow_gray(imgutil.invert(line))
plt.show()
