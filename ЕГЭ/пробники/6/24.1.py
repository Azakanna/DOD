f=open(r"C:\Users\hhov0\Downloads\24__1f0qr.txt")
s=f.readline()
a=sorted('qwertyuiopasdfghjklzxcvbnm')
b=[0]*26
mimimishka=10**8
maks=-10**8
for i in range(26):
    k=s.count(a[i])
    b[i]=k
for l in range(len(b)):
    if b[l]<mimimishka:
        mimimishka=b[l]
    if b[l]>maks:
        maks=b[l]
print(maks-mimimishka)