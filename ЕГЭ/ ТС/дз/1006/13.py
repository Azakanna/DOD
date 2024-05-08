f=open(r"C:\Users\hhov0\Downloads\17_1 (2).txt")
s=[int(x) for x in f]
kolvo=0
maks=-10**8
for i in range(len(s)-1):
    a=s[i]
    b=s[i+1]
    if a%2!=b%2:
        if (a%2==0 and a%6==0 and b%13==0) or (a%2!=0 and a%13==0 and b%6==0):
            kolvo+=1
            maks=max(maks,a+b)
print(kolvo,maks)

