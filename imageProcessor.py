import matplotlib.pyplot as plt
import numpy as np
import math
from PIL import Image, ImageDraw
from random import randrange

def drawHoughLine(a,b,width,height):
    x1 = 0
    y1 = round(b)
    x2 = width - 1
    y2 = round(a*x2 + b)
    
    img = Image.new(mode="L", size = (width, height), color=255)
    draw = ImageDraw.Draw(img)
    draw.line((x1, y1, x2, y2), fill=0)
    del draw
    return np.array(img)

def noiseImage(image, percent):
    img = image.copy()
    width = img.shape[1]
    height = img.shape[0]
    noisePoints = width * height * percent / 100
    print("percent of noise: " + str(percent))
    print("number of points of noise: " + str(noisePoints))
    for col in range(width):
        for i in range(math.ceil(noisePoints / width)):
            row = randrange(height)
            if (img[row,col] == 255):
                img[row,col] = 0
            else:
                img[row,col] = 255
    return img

def findFirstPixelInCol(col):
    i = 0
    while (col[i] == 255):
        if (i < len(col) - 1):
            i=i+1
        else:
            return -1
    return i

def findFirstPixelOfLine(img):
    coli = 0
    rowi = -1
    while (rowi == -1 and coli < img.shape[1]):
        col = img[:,coli]
        rowi = findFirstPixelInCol(col)
        coli = coli + 1
    if (rowi != -1):
        return [rowi, coli - 1]
    else:
        return [-1, -1]

def findLastPixelOfLine(img):
    coli = img.shape[1] - 1
    rowi = -1
    while (rowi == -1 and coli > 0):
        col = img[:,coli]
        rowi = findFirstPixelInCol(col)
        coli = coli - 1
    if (rowi != -1):
        return [rowi, coli - 1]
    else:
        return [-1, -1]
        

def calculateMiss(img1, img2):
    img1_first = findFirstPixelOfLine(img1)
    img1_last = findLastPixelOfLine(img1)
    img2_first = findFirstPixelOfLine(img2)
    img2_last = findLastPixelOfLine(img2)
    print("line 1: from " + str(img1_first) + " to " + str(img1_last))
    print("line 2: from " + str(img2_first) + " to " + str(img2_last))
    if (img2_first[0] == -1 or img2_last[0] == -1):
        return img1.shape[1]
    first_miss = abs(img2_first[0] - img1_first[0])
    last_miss = abs(img2_last[0] - img1_last[0])
    return max(first_miss, last_miss)
    
def showResults(y1, y2, x, path):
    plt.figure()
    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.title('Rozmiar błędu w pikslach w zależności od poziomu zaszumienia')
    plt.xlabel('Wielkość szumu w obrazie [% całego obrazu]')
    plt.ylabel('Błąd [px]')
    plt.legend(['Metoda ostra', 'Metoda rozmyta'], loc='upper left')
    plt.xlim([0, 100])
    plt.ylim([0, max(max(y1),max(y2))+1])
    plt.savefig(path + '/results.png')
    plt.show()
