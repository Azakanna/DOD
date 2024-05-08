def f(n):
    if n<6:
        return n
    if n>5 and n%2==0:
        return n+f(n//2)*2
    if n>5 and n%2==1:
        return f(n-2)+f(n-1)
def ff(k):
    summa=0
    h=str(k)
    for i in range(len(h)):
        summa+=int(h[i])
    return summa
for j in range(1,1001):
    g=f(j)
    if ff(g)==22:
        print(j)
        break



