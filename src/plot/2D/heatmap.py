import numpy as np
import matplotlib.pyplot as plt

ax = []
#C:/Users/kimtaeyoon/Documents/GitHub/GaussianProcessRegression/data/20211012/data/pre/3D/
a1 = np.loadtxt("C:/Users/kimtaeyoon/Documents/GitHub/GaussianProcessRegression/data/20211012/data/pre/3D/pre_s7_1.csv", delimiter=",", encoding='UTF8')
a2 = np.loadtxt("C:/Users/kimtaeyoon/Documents/GitHub/GaussianProcessRegression/data/20211012/data/pre/3D/pre_s7_2.csv", delimiter=",", encoding='UTF8')
a3 = np.loadtxt("C:/Users/kimtaeyoon/Documents/GitHub/GaussianProcessRegression/data/20211012/data/pre/3D/pre_s7_3.csv", delimiter=",", encoding='UTF8')
a4 = np.loadtxt("C:/Users/kimtaeyoon/Documents/GitHub/GaussianProcessRegression/data/20211012/data/pre/3D/pre_s7_4.csv", delimiter=",", encoding='UTF8')
a5 = np.loadtxt("C:/Users/kimtaeyoon/Documents/GitHub/GaussianProcessRegression/data/20211012/data/pre/3D/pre_s7_5.csv", delimiter=",", encoding='UTF8')


size_row = 0
for tmp in a1:    
    if a1[0][0] != tmp[0]:
        break
    size_row += 1



_Z1 = np.array([])
for temp in a1:
    _Z1 = np.append(_Z1, temp[2])
a11 = _Z1.reshape(-1, size_row)

fig = plt.figure()
ax.append(fig.add_subplot(1, 5, 1))
ax[0].set_title("(s7) Device 1")
plt.xlabel('X-Axis')
plt.imshow(a11, cmap='hot')




_Z2 = np.array([])
for temp in a2:
    _Z2 = np.append(_Z2, temp[2])
a22 = _Z2.reshape(-1, size_row)

ax.append(fig.add_subplot(1, 5, 2))
ax[1].set_title("Device 2")
plt.xlabel('X-Axis')
plt.imshow(a22, cmap='hot')




_Z3 = np.array([])
for temp in a3:
    _Z3 = np.append(_Z3, temp[2])
a33 = _Z3.reshape(-1, size_row)

ax.append(fig.add_subplot(1, 5, 3))
ax[2].set_title("Device 3")
plt.xlabel('X-Axis')
plt.imshow(a33, cmap='hot')




_Z4 = np.array([])
for temp in a4:
    _Z4 = np.append(_Z4, temp[2])
a44 = _Z4.reshape(-1, size_row)

ax.append(fig.add_subplot(1, 5, 4))
ax[3].set_title("Device 4")
plt.xlabel('X-Axis')
plt.imshow(a44, cmap='hot')




_Z5 = np.array([])
for temp in a5:
    _Z5 = np.append(_Z5, temp[2])
a55 = _Z5.reshape(-1, size_row)

ax.append(fig.add_subplot(1, 5, 5))
ax[4].set_title("Device 5")
plt.xlabel('X-Axis')
plt.imshow(a55, cmap='hot')




plt.tight_layout()
plt.show()
