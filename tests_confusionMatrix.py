import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import imageUtils as imgutil
import confusionMatrix as cm

img1 = Image.open('line_test_1.jpg').convert('L')
binimg1 = imgutil.binarize(imgutil.invert(img1),128)
img2 = Image.open('line_test_2.jpg').convert('L')
binimg2 = imgutil.binarize(imgutil.invert(img2),128)

conf = cm.getConfusionMatrix(binimg1,binimg2)
print(conf)
print("True Positive Rate: " + str(cm.getTPR(conf)))
print("False Positive Rate: " + str(cm.getFPR(conf)))
