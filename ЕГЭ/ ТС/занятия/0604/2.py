a=[0] * 10000000
a[3]=1
for i in range (3,97):
    if i == 25:
       a[i]=0
    if i == 12:
        for j in range (13,1000):
            a[j] = 0
    a[i+3] += a[i]
    a[i*2] += a[i]
    a[i**3] += a[i]
print(a[96])


