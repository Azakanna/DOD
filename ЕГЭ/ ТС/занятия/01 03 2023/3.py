print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x== (not y))<=(y and (not z)) or (z and (not w)))==0:
                    print(x,y,z,w)