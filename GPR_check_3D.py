data = "C:/Users/kimtaeyoon/Documents/GitHub/GaussianProcessRegression/data/20211012/data"
mode = "3D"
target = "i8_5"






import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d') # Axe3D object

a1 = np.loadtxt(data+"/pre/"+mode+"/pre_"+target+".csv", delimiter=",", encoding='UTF8')


_X = np.array([])
_Y = np.array([])
_Z1 = np.array([])


for temp in a1:
    _X = np.append(_X, temp[0])
    _Y = np.append(_Y, temp[1])
    _Z1 = np.append(_Z1, temp[2])



ax.scatter(_X, _Y, _Z1, cmap=plt.cm.Greens)
plt.title("three beacons")
plt.show()
