print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F=0
                if ((y<=x or z) and (z<=y))==F:
                    print(x,y,z,w,F)
    