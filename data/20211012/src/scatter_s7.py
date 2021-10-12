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

_X = np.array([])
_Y = np.array([])
_Z1 = np.array([])
_Z2 = np.array([])
_Z3 = np.array([])
_Z4 = np.array([])
_Z5 = np.array([])

for temp in a1:
    _X = np.append(_X, temp[0])
    _Y = np.append(_Y, temp[1])
    _Z1 = np.append(_Z1, temp[2])

for temp in a2:
    _Z2 = np.append(_Z2, temp[2])
for temp in a3:
    _Z3 = np.append(_Z3, temp[2])
for temp in a4:
    _Z4 = np.append(_Z4, temp[2])
for temp in a5:
    _Z5 = np.append(_Z5, temp[2])

ax.scatter(_X, _Y, _Z1, cmap=plt.cm.Greens)
ax.scatter(_X, _Y, _Z2, cmap=plt.cm.Greens)
ax.scatter(_X, _Y, _Z3, cmap=plt.cm.Greens)
ax.scatter(_X, _Y, _Z4, cmap=plt.cm.Greens)
ax.scatter(_X, _Y, _Z5, cmap=plt.cm.Greens)
plt.title("5 Devices (s7)")
plt.show()
