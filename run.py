from PIL import Image
import matplotlib.pyplot as plt
import imageUtils as imgutil
from houghSpace import HoughSpace
import math
import numpy as np
import imageProcessor as ip
import sys
import confusionMatrix as cm
from pathlib import Path

out_dir = "output_" + sys.argv[1].split(".")[0]
Path(out_dir).mkdir(parents=True, exist_ok=True)
imgName = sys.argv[1]
img = Image.open(imgName).convert('L')
binimg = imgutil.binarize(img,195)
#binimg = imgutil.invert(binimg)
imgutil.imshow_gray(binimg)
plt.show()
results_sharp = []
results_blurred = []
results_x = []
for i in range(1,90,2):
    image = ip.noiseImage(binimg,i)
    noised_image = Image.fromarray(image.astype('uint8'))
    noised_image.save(out_dir + "/input_"+str(i)+"_percent.png")

    hough = HoughSpace(image)
    [a,b] = hough.getLineParams()
    line_sharp = ip.drawHoughLine(a,b,binimg.shape[1],binimg.shape[0])
    sharp_image = Image.fromarray(line_sharp)
    sharp_image.save(out_dir + "/output_sharp_"+str(i)+"_percent.png")
    hough.saveHoughSpace(out_dir + "/hough_sharp_"+str(i)+"_percent.png")

    mask = np.matrix([[1, 2, 1],[2,4,2],[1,2,1]], dtype=np.uint8)
    hough.convolveHoughSpace(mask)
    hough.saveHoughSpace(out_dir + "/hough_blurred_"+str(i)+"_percent.png")
    [a,b] = hough.getLineParams()
    line = ip.drawHoughLine(a,b,binimg.shape[1],binimg.shape[0])
    imgutil.imshow_gray(line)
    output = Image.fromarray(line)
    output.save(out_dir + "/output_"+str(i)+"_percent.png")
    results_sharp.append(ip.calculateMiss(binimg,line_sharp))
    results_blurred.append(ip.calculateMiss(binimg,line))
    results_x.append(i)
    print("------------------------------------")
for i in range(len(results_x)):
    print("sharp: " + str(results_sharp[i]) + "\t blurred: " + str(results_blurred[i]))
ip.showResults(results_sharp, results_blurred, results_x, out_dir)
