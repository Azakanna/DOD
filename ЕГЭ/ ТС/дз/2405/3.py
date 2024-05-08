def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for l in range(3,100):
    if prime(l)==True:
        N=l**4*2
        if 10_000_000 <= N <= 50_000_000:
            print(N,l)