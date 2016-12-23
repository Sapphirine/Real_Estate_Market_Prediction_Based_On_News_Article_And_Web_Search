# Generate SVR prediction model based on Web Articles

import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import csv

f = open( "hpi.txt", "r" )
lines = f.read().split('\n')
print lines
length = len(lines)
data = np.array([((float(item[0:6]))) for item in lines])
f.close()

f = open( "senti1.txt", "r" )
lines = f.read().split('\n')
ydata = np.array([float(item[0:6]) for item in lines])
f.close()

X = ydata
y = data

#svr_rbf = SVR(kernel='rbf', C=1e1, gamma=0.2)
svr_lin = SVR(kernel='linear', C=1e3)
#svr_poly = SVR(kernel='poly', C=1, degree=2)
x2 = np.array([[i] for i in range(length,length+10)])
#y_rbf = svr_rbf.fit(X, y).predict(x2)
y_lin = svr_lin.fit(X, y).predict(x2)
#y_poly = svr_poly.fit(X, y).predict(x2)

lw = 2
plt.scatter(X, y, color='darkorange', label='data')
plt.hold('on')
#plt.plot(x2, y_rbf, color='navy', lw=lw, label='RBF model')
plt.plot(x2,y_lin, color='c', lw=lw, label='Linear model')
#plt.plot(x2, y_poly, color='cornflowerblue', lw=lw, label='Polynomial model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('SVR')
plt.show()