import numpy as np
import math
import imageUtils
from PIL import Image

def convolve(img,mask):
    img = np.asarray(img)
    size = img.shape
    acc = np.zeros((size[0],size[1]))
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
    if normalize == True:
        print('normalizing...')
    else: 
        print('not normalizing...')
    for row in range(1,size[0]-1):
        for column in range(1,size[1]-1):
            val=0;
            for i in range(-1,2):
                for j in range(-1,2):
                    val=np.floor(val+img[row+i,column+j] * mask[i+1,j+1])
            if val>4080:
                print("val overflow: " + str(val))
            if normalize:
                val = 1.0 * val / sumMask
            else:
                val = (val - minMask)/(maxMask - minMask)
            
#            val = np.floor(val).astype(np.uint8);
            acc[row,column] = val
    maxVal = np.amax(acc)
    for row in range(1,size[0]-1):
        for column in range(1,size[1]-1):
            outImg[row,column] = (maxVal / 255) * acc[row,column]
    res = np.reshape(outImg,(size[0],size[1]))
    res = Image.fromarray(res)
    return res

def convolve2d(image, kernel):
    # This function which takes an image and a kernel 
    # and returns the convolution of them
    # Args:
    #   image: a numpy array of size [image_height, image_width].
    #   kernel: a numpy array of size [kernel_height, kernel_width].
    # Returns:
    #   a numpy array of size [image_height, image_width] (convolution output).
    
    kernel = np.flipud(np.fliplr(kernel))    # Flip the kernel
    output = np.zeros_like(image)            # convolution output
    # Add zero padding to the input image
    image_padded = np.zeros((image.shape[0] + 2, image.shape[1] + 2))   
    image_padded[1:-1, 1:-1] = image
    for x in range(image.shape[1]):     # Loop over every pixel of the image
        for y in range(image.shape[0]):
            # element-wise multiplication of the kernel and the image
            output[y,x]=(kernel*image_padded[y:y+3,x:x+3]).sum()        
    return Image.fromarray(output)
