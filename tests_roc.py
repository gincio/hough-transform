import roc
import confusionMatrix as cm

confusion = [[249499, 1, 0, 500],
[249499, 1, 0, 500],
[249100, 400, 399, 101],
[249499, 1, 0, 500],
[249499, 1, 0, 500]]
tprs = []
fprs = []
for i in range(5):
    tprs.append(cm.getTPR(confusion[i]))
    fprs.append(cm.getFPR(confusion[i]))

roc_pts = roc.calculateROC(tprs, fprs)
roc.showROC(roc_pts)
