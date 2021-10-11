data = "C:/Users/kimtaeyoon/Desktop/data"
mode = "2D"
target = "i8_1"






import matplotlib.pyplot as plt
import numpy as np 

fig = plt.figure(figsize=(10, 5))

a1 = np.loadtxt(data+"/ori/"+mode+"/"+target+".csv", delimiter=",", encoding='UTF8')
a2 = np.loadtxt(data+"/pre/"+mode+"/pre_"+target+".csv", delimiter=",", encoding='UTF8')


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


plt.errorbar(_X1, _Z1, 1, label='origin')
plt.plot(_X2, _Z2, label='predicted')
plt.legend()
plt.title("Device 1 Comparison")
plt.show()
