import matplotlib.pyplot as plt
import numpy as np
import math
from PIL import Image, ImageDraw

def drawline(r,theta):
    a=math.cos(np.deg2rad(theta))
    b=math.sin(np.deg2rad(theta))
    x0=r*a
    y0=r*b
    x1=int(x0+500*(-b))
    y1=int(y0+500*(a))
    x2=int(x0-500*(-b))
    y2=int(y0-500*(a))
    plt.plot([x1,x2],[y1,y2])
    plt.show()

def calculateline(a,b, width, height):
    img = np.zeros((width,height))
    for x in range(width):
        y = round(a*x + b)
        if y >= height: break
        if y >= 0:
            img[x,y] = 255  
    return img

def drawHoughLine(a,b,width,height):
    if (a < 1):
        x1 = 0
        y1 = round(b)
        x2 = width - 1
        y2 = round(a*x2 + b)
    else:
        y1 = 0
        x1 = round((-b)/a)
        y2 = height - 1
        x2 = round((y2 - b)/a)

    img = Image.new(mode="L", size = (width, height), color=255)
    draw = ImageDraw.Draw(img)
    draw.line((x1, y1, x2, y2), fill=0)
    del draw
    return img.asarray
