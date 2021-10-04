import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import numpy as np 
from PIL import Image



fig = plt.figure(figsize=(10, 10))
#ax = fig.add_subplot(111, projection='3d') # Axe3D object

a1 = np.loadtxt("Z:/HDD1/Data/광운대학교/2021_딥러닝세미나/20210930/data/pre/3D/pre_i8_1_5.csv", delimiter=",", encoding='UTF8')
a2 = np.loadtxt("Z:/HDD1/Data/광운대학교/2021_딥러닝세미나/20210930/data/pre/3D/pre_i8_2_5.csv", delimiter=",", encoding='UTF8')
a3 = np.loadtxt("Z:/HDD1/Data/광운대학교/2021_딥러닝세미나/20210930/data/pre/3D/pre_i8_4_5.csv", delimiter=",", encoding='UTF8')
a4 = np.loadtxt("Z:/HDD1/Data/광운대학교/2021_딥러닝세미나/20210930/data/pre/3D/pre_i8_5_5.csv", delimiter=",", encoding='UTF8')



size_row = 0
for tmp in a1:    
    if a1[0][0] != tmp[0]:
        break
    size_row += 1

image = Image.new("RGB", (size_row,int(len(a1)/size_row)), (0,0,0))
im = image.load()
(width, height) = image.size



_X1 = np.array([])
_X2 = np.array([])
_X3 = np.array([])
_X4 = np.array([])

_Y1 = np.array([])
_Y2 = np.array([])
_Y3 = np.array([])
_Y4 = np.array([])

_Z1 = np.array([])
_Z2 = np.array([])
_Z3 = np.array([])
_Z4 = np.array([])

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


i = 0
idx=0
for i in range(0,height):
    for j in range(0,width):
        tmax = max(_Z1[idx], _Z2[idx], _Z3[idx], _Z4[idx])
        #print(tmax)
        if(tmax == _Z1[idx]):
            color = (0,0,0)
        if(tmax == _Z2[idx]):
            color = (0,0,200)
        if(tmax == _Z3[idx]):
            color = (0,200,0)
        if(tmax == _Z4[idx]):
            color = (200,0,0)
        im[j,i] = color

        idx+=1
#print(idx)



image.save("map_i8.jpg")

