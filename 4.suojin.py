for a in range(1,10,1):
    for b in range(1,10,1):
        print('{}*{}='.format(a,b)+str(a*b))

for i in range(1,10):
     for j in range(i,10):
        print("%d*%d=%2d" % (i,j,i*j),end=" ")
     print("")