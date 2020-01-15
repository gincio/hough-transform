import numpy as np
import math
import imageUtils
from PIL import Image

def convolve(img,mask):
    img = np.asarray(img)
    size = img.shape
    outImg = np.zeros((size[0],size[1]),dtype=np.uint8)
    normalize = True
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if mask[i,j] > 0: continue
            nomalize = False
    
    if normalize:
        sumMask = np.sum(np.sum(mask))
    else:
        maxMask = np.amax(mask)
        minMask = np.amin(mask)
    
    for row in range(1,size[0]-1):
        for column in range(1,size[1]-1):
            val=0;
            for i in range(-1,2):
                for j in range(-1,2):
                    val=val+img[row+i,column+j] * mask[i+1,j+1]

            if normalize:
                val = val / sumMask
            else:
                val = (val - minMask)/(maxMask - minMask)

            val = val.round().astype(np.uint8);
            outImg[row,column] = val
    res = np.reshape(outImg,(size[0],size[1]))
    res = Image.fromarray(res)
    return res
