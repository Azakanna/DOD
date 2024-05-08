def f(n):
    if n>32:
        return n*n*n
    else:
        return f(n*2)+(n//3)*n
kolvo=0
for i in range(1,1001):
    a=f(i)
    if a%10==3:
        kolvo+=1
print(kolvo)
