print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F=0
                if (((z or (not y)) and ((not x) or (not w))) or ((z==w) or (y and (not x))))==F:
                    print(x,y,z,w,F)