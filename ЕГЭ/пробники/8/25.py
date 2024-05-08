# 150_000_000 300_000_000
a=[]
b=[]
for m in range(1,100,2):
    for n in range(0,100,2):
        N=(2**m)*(3**n)
        if 150_000_000 <= N <= 300_000_000:
            a.append(N)
            b.append(n+m)
print(a,b)
