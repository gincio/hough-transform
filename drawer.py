import matplotlib.pyplot as plt
import numpy as np
import math

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
