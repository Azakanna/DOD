f=open(r"C:\Users\hhov0\Downloads\17_3 (2).txt")
s=[int(x) for x in f]
srar=sum(s)/len(s)
kolvo=0
otv=-10**8
for i in range(len(s)-1):
    if (s[i]>srar and s[i+1] >srar) and abs(s[i]+s[i+1])%100==31:
        kolvo+=1
        otv=max(otv,s[i]+s[i+1])
print(kolvo,otv)
