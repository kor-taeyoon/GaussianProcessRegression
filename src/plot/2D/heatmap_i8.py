import numpy as np
import matplotlib.pyplot as plt

ax = []

a1 = np.loadtxt("Z:/HDD1/Data/광운대학교/2021_딥러닝세미나/20210930/data/pre/3D/pre_i8_1_5.csv", delimiter=",", encoding='UTF8')
a2 = np.loadtxt("Z:/HDD1/Data/광운대학교/2021_딥러닝세미나/20210930/data/pre/3D/pre_i8_2_5.csv", delimiter=",", encoding='UTF8')
a3 = np.loadtxt("Z:/HDD1/Data/광운대학교/2021_딥러닝세미나/20210930/data/pre/3D/pre_i8_4_5.csv", delimiter=",", encoding='UTF8')
a4 = np.loadtxt("Z:/HDD1/Data/광운대학교/2021_딥러닝세미나/20210930/data/pre/3D/pre_i8_5_5.csv", delimiter=",", encoding='UTF8')


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
ax.append(fig.add_subplot(1, 4, 1))
ax[0].set_title("(i8) Device 1")
plt.xlabel('X-Axis')
plt.imshow(a11, cmap='hot')




_Z2 = np.array([])
for temp in a2:
    _Z2 = np.append(_Z2, temp[2])
a22 = _Z2.reshape(-1, size_row)

ax.append(fig.add_subplot(1, 4, 2))
ax[1].set_title("Device 2")
plt.xlabel('X-Axis')
plt.imshow(a22, cmap='hot')




_Z3 = np.array([])
for temp in a3:
    _Z3 = np.append(_Z3, temp[2])
a33 = _Z3.reshape(-1, size_row)

ax.append(fig.add_subplot(1, 4, 3))
ax[2].set_title("Device 4")
plt.xlabel('X-Axis')
plt.imshow(a33, cmap='hot')




_Z4 = np.array([])
for temp in a4:
    _Z4 = np.append(_Z4, temp[2])
a44 = _Z4.reshape(-1, size_row)

ax.append(fig.add_subplot(1, 4, 4))
ax[3].set_title("Device 5")
plt.xlabel('X-Axis')
plt.imshow(a44, cmap='hot')




plt.tight_layout()
plt.show()
