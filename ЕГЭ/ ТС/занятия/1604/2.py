def check(a):
    for x in range(1,1000):
        if ((x%a!=0)<=((x%6==0)<=(x%9!=0)))==False:
            return False
    return True
for a in range(1,1000):
    if check(a)==True:
        print(a)

