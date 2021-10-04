import matplotlib.pyplot as plt
import numpy as np 

fig = plt.figure(figsize=(10, 5))


a1 = np.loadtxt("Z:/HDD1/Data/광운대학교/2021_딥러닝세미나/20210930/data/ori/2D_all/tag.csv", delimiter=",", encoding='UTF8')
a2 = np.loadtxt("Z:/HDD1/Data/광운대학교/2021_딥러닝세미나/20210930/data/pre/2D/pre_all_tag.csv", delimiter=",", encoding='UTF8')


_X1 = np.array([])
_X2 = np.array([])
_Z1 = np.array([])
_Z2 = np.array([])


for temp in a1:
    _X1 = np.append(_X1, temp[3])
    _Z1 = np.append(_Z1, temp[2])
for temp in a2:
    _X2 = np.append(_X2, temp[0])
    _Z2 = np.append(_Z2, temp[1])


#line1 = plt.plot(_X2, _Z2, label='predicted')
line1 = plt.errorbar(_X2, _Z2, 5, label='predicted')
plt.setp(line1, color='darkorange', alpha=0.75)

#line2 = plt.plot(_X1, _Z1, label='origin')
line2 = plt.errorbar(_X1, _Z1, 0, label='origin')
plt.setp(line2, color='royalblue')

#plt.setp(line2, linewidth=15.0, alpha=0.2)
plt.legend()
plt.title("Predict Result (tag)")
plt.show()
