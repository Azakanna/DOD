def check(a):
    for x in range(1, 500):
        for y in range(1, 500):
            if ((x*y>a)or(27>y)or(y-20>=a)or(x<8))==False:
                return False
    return True
for a in range(-100,500):
    if check(a)==True:
        print(a)