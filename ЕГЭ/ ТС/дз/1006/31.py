# def f(a,n):
#     return sum(a[::-1][i]*n**i for i in range(len(a)))
# for p in range(100,1000):
#     q=int(str(p)[::-1])
#     if f([9,6,1],p)==f([1,6,9],q):
#         print(p,q)
for p in range(100,1000):
    for q in range(100,1000):
        a=9*p**2+6*p+1
        b=1*q**2+6*q+9
        if a==b:
            z=p
            x=str(q)[::-1]
            if z==int(x):

                print(p,q)