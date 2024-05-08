print('x y z F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F=1
            if ((x and (not y) and (not z)) or (x and y and (not z)) or ((not x) and y and z))==F:
                print(x,y,z,F)