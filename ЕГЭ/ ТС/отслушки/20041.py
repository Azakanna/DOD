def check(a):
    for x in range(1,1000):
        if ((x&a!=0)<=((x&25==0)<=(x&17!=0)))==0:
            return False
    return True
for a in range(-100,1000):
    if check(a)==True:
        print(a)
