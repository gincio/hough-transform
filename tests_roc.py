import roc
tprs = [0, 0.4, 0.7, 0.8, 0.87, 0.91, 0.96, 0.97, 0.98, 1]
fprs = [0, 0.04, 0.06, 0.1, 0.23, 0.4, 0.7, 0.8, 0.9, 1]
roc_pts = roc.calculateROC(tprs, fprs)
roc.showROC(roc_pts)
