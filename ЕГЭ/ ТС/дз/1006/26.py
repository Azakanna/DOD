def f(x):
    d=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
a=[]
for x in range(2,1000):
    d=f(x)
    if d==[]:
        a.append(x**2)
for x in range(21318,80000):
    d=f(x)
    k=0
    for i in d:
        if i in a:
            k+=1
    if k>=3:
        print(x)