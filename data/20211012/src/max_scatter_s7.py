import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d') # Axe3D object

a1 = np.loadtxt("C:/Users/kimtaeyoon/Documents/GitHub/GaussianProcessRegression/data/20211012/data/pre/3D/pre_s7_1.csv", delimiter=",", encoding='UTF8')
a2 = np.loadtxt("C:/Users/kimtaeyoon/Documents/GitHub/GaussianProcessRegression/data/20211012/data/pre/3D/pre_s7_2.csv", delimiter=",", encoding='UTF8')
a3 = np.loadtxt("C:/Users/kimtaeyoon/Documents/GitHub/GaussianProcessRegression/data/20211012/data/pre/3D/pre_s7_3.csv", delimiter=",", encoding='UTF8')
a4 = np.loadtxt("C:/Users/kimtaeyoon/Documents/GitHub/GaussianProcessRegression/data/20211012/data/pre/3D/pre_s7_4.csv", delimiter=",", encoding='UTF8')
a5 = np.loadtxt("C:/Users/kimtaeyoon/Documents/GitHub/GaussianProcessRegression/data/20211012/data/pre/3D/pre_s7_5.csv", delimiter=",", encoding='UTF8')

_X1 = np.array([])
_X2 = np.array([])
_X3 = np.array([])
_X4 = np.array([])
_X5 = np.array([])
_Y1 = np.array([])
_Y2 = np.array([])
_Y3 = np.array([])
_Y4 = np.array([])
_Y5 = np.array([])
_Z1 = np.array([])
_Z2 = np.array([])
_Z3 = np.array([])
_Z4 = np.array([])
_Z5 = np.array([])

for temp in a1:
    _X1 = np.append(_X1, temp[0])
    _Y1 = np.append(_Y1, temp[1])
    _Z1 = np.append(_Z1, temp[2])
for temp in a2:
    _X2 = np.append(_X2, temp[0])
    _Y2 = np.append(_Y2, temp[1])
    _Z2 = np.append(_Z2, temp[2])
for temp in a3:
    _X3 = np.append(_X3, temp[0])
    _Y3 = np.append(_Y3, temp[1])
    _Z3 = np.append(_Z3, temp[2])
for temp in a4:
    _X4 = np.append(_X4, temp[0])
    _Y4 = np.append(_Y4, temp[1])
    _Z4 = np.append(_Z4, temp[2])
for temp in a5:
    _X5 = np.append(_X5, temp[0])
    _Y5 = np.append(_Y5, temp[1])
    _Z5 = np.append(_Z5, temp[2])

i = 0
is1 = []
is2 = []
is3 = []
is4 = []
is5 = []
for x in a1:
    tmax = max(_Z1[i], _Z2[i], _Z3[i], _Z4[i], _Z5[i])
    if(tmax != _Z1[i]):
        is1.append(i)
    if(tmax != _Z2[i]):
        is2.append(i)
    if(tmax != _Z3[i]):
        is3.append(i)
    if(tmax != _Z4[i]):
        is4.append(i)
    if(tmax != _Z5[i]):
        is5.append(i)
    i+=1


_X1 = np.delete(_X1, is1)
_X2 = np.delete(_X2, is2)
_X3 = np.delete(_X3, is3)
_X4 = np.delete(_X4, is4)
_X5 = np.delete(_X5, is5)

_Y1 = np.delete(_Y1, is1)
_Y2 = np.delete(_Y2, is2)
_Y3 = np.delete(_Y3, is3)
_Y4 = np.delete(_Y4, is4)
_Y5 = np.delete(_Y5, is5)

_Z1 = np.delete(_Z1, is1)
_Z2 = np.delete(_Z2, is2)
_Z3 = np.delete(_Z3, is3)
_Z4 = np.delete(_Z4, is4)
_Z5 = np.delete(_Z5, is5)

ax.scatter(_X1, _Y1, _Z1, cmap=plt.cm.Greens, s = 100)
ax.scatter(_X2, _Y2, _Z2, cmap=plt.cm.Greens, s = 100)
ax.scatter(_X3, _Y3, _Z3, cmap=plt.cm.Greens, s = 100)
ax.scatter(_X4, _Y4, _Z4, cmap=plt.cm.Greens, s = 100)
ax.scatter(_X5, _Y5, _Z5, cmap=plt.cm.Greens, s = 100)
plt.title("5 Beacons (s7)")
plt.show()
