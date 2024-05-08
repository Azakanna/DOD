def f(n):
    if n==0:
        return 0
    if n%3 == 0 and n%2 !=0 and n % 5 !=0:
        return  3*f(n//3)
    if n % 3!= 0 and n % 5 != 0 and n%2 ==0:
        return 2*f(n//2)
    if n%5==0 and n%3 !=0 and n%3 !=0:
        return 5*f(n//5)
    else:
        return 2*n
summa=0
for m in range(1000000):
    if 1000<=f(m)<=3000:
        if m%2==0:
            summa += m
print(summa)


