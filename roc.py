import numpy as np
import matplotlib.pyplot as plt

def calculateROC(tprs, fprs):
    count = len(tprs)
    roc_pts = np.zeros((2,count))
    for i in range(count):
        roc_pts[0,i] = fprs[i]
        roc_pts[1,i] = tprs[i]
    return roc_pts

def showROC(roc_pts):
    x = roc_pts[0,:]
    y = roc_pts[1,:]
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.plot(x,y)
    plt.title("Krzywa ROC")
    plt.xlabel("FPR")
    plt.ylabel("TPR")
    plt.show()
    plt.close()
