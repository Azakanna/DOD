a=[0]*1000
a[12]=1
for i in range(12,97):
    if  i ==30:
        for j in range(31,100):
            a[j]=0
    a[i+3]+=a[i]
    a[i*2]+=a[i]
print(a[96])