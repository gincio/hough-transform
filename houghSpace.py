import numpy as np
import matplotlib.pyplot as plt
import math
import convolution

class HoughSpace:
    def __init__(self, img):
        self.img = img
        # store image size
        img_shape = img.shape
        self.img_width = img_shape[0]
        self.img_height = img_shape[1]
        # prepare variables for transform
        self.r_min = 0.0
        self.r_max = math.hypot(self.img_width, self.img_height)
        self.theta_min = 0.0
        self.theta_max = 1.0 * math.pi
        self.r_dim = math.ceil(self.r_max * 2)
        self.theta_dim = 720
        self.hough_space = np.zeros((self.r_dim,self.theta_dim))
        self.doHoughTransform()

    def index2radius(self,ind):
        print("index " + str(ind) + " / " + str(self.r_dim))
        print("position " + str(ind / self.r_dim))
        print("length " + str(ind / self.r_dim * self.r_max))
        return ind / self.r_dim

    def radius2index(self,r):
        return math.floor(self.r_dim * ( 1.0 * r ) / self.r_max)

    def index2angle(self,ind):
        return 1.0 * ind * self.theta_max / self.theta_dim

    def angle2index(self,theta):
        return (theta / self.theta_max) * self.theta_dim

    def doHoughTransform(self):
        for x in range(self.img_width):
            for y in range(self.img_height):
                if self.img[x,y] == 255: continue
                for itheta in range(self.theta_dim):
                    theta = self.index2angle(itheta)
                    r = x * math.cos(theta) + y * math.sin(theta)
                    ir = self.radius2index(r)
                    self.hough_space[ir,itheta] = self.hough_space[ir,itheta] + 1

    def showHoughSpace(self):
        plt.imshow(self.hough_space)
        plt.xlim(0,self.theta_dim)
        plt.ylim(0,self.r_dim)

        tick_locs = [i for i in range(0,self.theta_dim,100)]
        tick_lbls = [round( (1.0 * i * self.theta_max) / self.theta_dim,1) for i in range(0,self.theta_dim,100)]
        plt.xticks(tick_locs, tick_lbls)

        tick_locs = [i for i in range(0,self.r_dim,200)]
        tick_lbls = [round( (1.0 * i * self.r_max ) / self.r_dim,1) for i in range(0,self.r_dim,200)]
        plt.yticks(tick_locs, tick_lbls)

        plt.xlabel(r'Kąt')
        plt.ylabel(r'Promień')
        plt.title('Przestrzeń Hougha')
        plt.show()
        plt.close()

    def convolveHoughSpace(self, mask):
        self.hough_space = np.asarray(convolution.convolve(self.hough_space,mask))

    def getMaxPosition(self):
        maxVal = np.amax(self.hough_space)
        maxPos = [-1,-1]
        for x in range(self.r_dim):
            for y in range(self.theta_dim):
                if self.hough_space[x][y] == maxVal:
                    maxPos = [x, y]
                    print(maxPos)
                    return maxPos
        return maxPos

    def getAngle(self,position):
        ind = position[1]
        return self.index2angle(ind)
    
    def getRadius(self,position):
        ind = position[0]
        return self.index2radius(ind)*500

    def getLineParams(self):
        maxPos = self.getMaxPosition()
        r = self.getRadius(maxPos)
        angle = self.getAngle(maxPos)
        print("angle: " + str(np.rad2deg(angle)))
        print("radius: " + str(r))
        a = -1.0 * math.cos(angle) / math.sin(angle)
        b = r / math.sin(angle)
        print("Found line: y = " + str(a) + "x + " + str(b))
        return a,b
