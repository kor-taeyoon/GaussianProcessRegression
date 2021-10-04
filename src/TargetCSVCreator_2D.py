dist_start = 1
dist_final = 10
step = 1



f = open("tar_2D.csv", "w")
for i in range(dist_start, dist_final+1, step):
    f.write(str(i)+','+'\n')
f.close()