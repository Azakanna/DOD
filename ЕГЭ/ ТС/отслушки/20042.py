def check(a):
    for x in range(1,1000):
        if (((x&47!=0)or(x&24!=0))<=((x&29==0)<=(x&a!=0)))==0:
            return False
    return True
for a in range(1,1000):
    if check(a)==True:
        print(a)
