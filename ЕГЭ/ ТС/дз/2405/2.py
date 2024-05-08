def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for l in range(3,100):
    if prime(l)==True:
        for o in range(100):
            N=l**10*2**o
            if 20_000_000 <= N <= 80_000_000:
                print(N,l,o)