def check(a):
    for x in range(1000):
        if ((x&144==0)<=((x&220!=0)<=(x&a!=0)))==0:
            return False
    return True
for a in range(1000):
    if check(a)==True:
        print(a)
        break