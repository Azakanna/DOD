print('x y z ')
for x in range(2):
    for y in range(2):
        for z in range(2):
            # for w in range(2):
            f= ((x<=(not y))<=(not z))==(x and (not y))
            if f==1:
                print(x,y,z,f)