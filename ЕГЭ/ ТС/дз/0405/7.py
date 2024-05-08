f=open(r'C:\Users\hhov0\Downloads\17_3 (1).txt')
a = [int(x) for x in f]
kolvo=0
maksum=-10*8
srarf=sum(a)/len(a)
for l in range(len(a)-1):
    if (a[l]<srarf and a[l+1]>srarf) or (a[l]>srarf and a[l+1]<srarf):
        kolvo+=1
        if a[l]+a[l+1]>maksum:
            maksum=a[l]+a[l+1]
print(kolvo,maksum)