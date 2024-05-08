f=open(r"C:\Users\hhov0\Downloads\17_4 (1).txt")
s=[int(x) for x in f]
kolvo=0
otv=-10**8
maks=-10**8
for i in range(len(s)):
    if s[i]%171==0:
        maks=max(maks,s[i])
for l in range(len(s)-1):
    if (s[l] < maks or s[l+1] <maks):
        if s[l]%2==1 or s[l+1]%2==1:
            kolvo+=1
            otv=max(otv,s[l]+s[l+1])
print(kolvo,otv)
