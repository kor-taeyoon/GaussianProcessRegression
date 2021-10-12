x_start = 156
x_final = 1490
y_start = 11
y_final = 846
step = 10



f = open("tar_3D_"+str(step)+".csv", "w")
for i in range(x_start, x_final+1, step):
    for j in range(y_start, y_final+1, step):
        f.write(str(i)+','+str(j)+'\n')
f.close()