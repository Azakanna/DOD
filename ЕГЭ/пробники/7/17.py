f=open(r"C:\Users\hhov0\Downloads\17-290__yrq3.txt")
s=[int(x) for x in f.readlines()]
kolvo=0
maks=-10**8

def ss6(n):
    dl=0
    while n>0:
        a=n%6
        dl+=1
        n=n//6
    return dl==4
for i in range(len(s)-2):
    if (s[i]%5==1 or s[i+1]%5==1 or s[i+2]%5==1) \
            and ss6(s[i])==True and ss6(s[i+1])==True  and ss6(s[i+2])==True:
        kolvo+=1
        u=(max(s[i],s[i+1],s[i+2]))-(min(s[i],s[i+1],s[i+2]))
        maks=max(u,maks)
print(kolvo,maks)
