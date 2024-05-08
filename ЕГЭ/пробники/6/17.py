from math import sqrt
f=open(r"C:\Users\hhov0\Downloads\17__1f0qm.txt")
s=[int(x) for x in f]
a=[]
kolvo=0
maks=-10**8
for i in range(len(s)):
    if sqrt(s[i])%1==0:
        a.append(s[i])
for l in range(len(a)):
    for k in range(l+1,len(a)):
        A=a[l]+a[k]
        if A in s:
            ind=sorted([s.index(a[l]),s.index(a[k]),s.index(A)])
            if ind[0]+100<=ind[1] and ind[1]+100<=ind[2]:
                kolvo+=1
                if A>maks:
                    maks=A
print(kolvo,maks)









