f=open(r'C:\Users\hhov0\Downloads\17_4.txt')
a = [int(x) for x in f]
kolvo=0
maks=-10**8

for i in range(len(a)-1):
    if ((a[i]%2==0 and a[i]%6==0) and (a[i+1]%2!=0 and a[i+1]%13==0)) \
            or ((a[i]%2!=0 and a[i]%13==0) and (a[i+1]%2==0 and a[i+1]%6==0)):
        kolvo+=1
        if a[i]+a[i+1]>maks:
            maks=a[i]+a[i+1]
print(kolvo,maks)
