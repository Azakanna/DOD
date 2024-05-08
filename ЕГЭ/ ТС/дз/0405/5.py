f=open(r'C:\Users\hhov0\Downloads\17_1 (1).txt')
a = [int(x) for x in f]
minim=10**8
kolvo=0
for i in range(len(a)-1):
    if (a[i]*a[i+1])%2!=0 and (a[i]+a[i+1])%7!=0:
        kolvo+=1
    if a[i]+a[i+1]<minim:
        minim=a[i]+a[i+1]
print(kolvo,minim)