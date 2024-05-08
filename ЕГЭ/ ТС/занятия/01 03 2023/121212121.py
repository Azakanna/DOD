print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (x and y and  (not w)) or (x and y and z  and  (not w)) or (x and (not y)  and (not z) and (not w))==1:
                    print(x, y, z, w)








