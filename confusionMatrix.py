import numpy as np

def getConfusionMatrix(original, detected):
    tp = 0
    fp = 0
    fn = 0
    tn = 0
    original = np.asarray(original)
    detected = np.asarray(detected)
    size = original.shape
    for row in range(size[0]):
        for col in range(size[1]):
#            print("[" + str(row) + "," + str(col) + "] : " + str(original[row,col]) + " , " + str(detected[row,col]))
            if original[row,col] != 0 and detected[row,col] != 0:
                tp = tp + 1
            if original[row,col] != 0 and detected[row,col] == 0:
                fn = fn + 1
            if original[row,col] == 0 and detected[row,col] != 0:
                fp = fp + 1
            if original[row,col] == 0 and detected[row,col] == 0:
                tn = tn + 1
    return [tp, fp, fn, tn]

def getTPR(confusionMatrix):
    tp = confusionMatrix[0]
    cp = tp + confusionMatrix[2]
    return tp / cp

def getFPR(confusionMatrix):
    fp = confusionMatrix[1]
    cn = fp + confusionMatrix[3]
    return fp / cn
