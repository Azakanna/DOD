f=open(r"C:\Users\hhov0\Downloads\8.txt")
s=f.readline()
alf=sorted('QWERTYUIOPASDFGHJKLZXCVBNM')
a=[0]*26
for i in range(26):
    a[i]=s.count(alf[i])
maks=max(a)
for l in range(26):
    if a[l]==maks:
        print(alf[l])