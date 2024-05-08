def check(a):
    for x in range(1,500):
        for y in range(1, 500):
            if ((a<x+y)or (x>=48) or (y>2))==False:
                return False
    return True
for a in range(-100,500):
    if check(a)==True:
        print(a)