def f(n):
    if n<3:
        return 2*n*n+2
    if n>2 and n%5==0:
        return 2*f(n-2)+f(n/2)+n
    if n>2 and n%5!=0:
        return n*n+f(n-2)+1+f(n/3)
kolvo=0
for i in range(1,301):
    a=f(i)
    if a>10**5:
        kolvo+=1
print(kolvo)