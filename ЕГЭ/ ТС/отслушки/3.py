print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (((y or z) <= x) or (x == y)) == 0:
                print(x, y, z)