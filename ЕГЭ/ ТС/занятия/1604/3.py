def check(a):
    for x in range(1,20000):
        if ((((x%a==0)and(x%36==0))<=(x%324==0))and(a>100))==False:
            return False
    return True
for a in range(1,20000):
    if check(a)==True:
        print(a)
        break