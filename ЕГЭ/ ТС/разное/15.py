def f(a):
    for x in range (1,1000):
        if (((x%19!=0) or (x%15!=0))<=(x%a!=0))==0:
            return 0
    return 1
for a in range (1,1000):
    if f(a)==1:
        print(a)
        break
