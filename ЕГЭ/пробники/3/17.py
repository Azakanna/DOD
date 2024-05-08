f=open(r"C:\Users\hhov0\Downloads\17__19rqi__1a44j.txt")
x=[int(x) for x in f]
kolvo=0
maximus=0
for i in range(len(x)-1):
    if (x[i]+x[i+1])%2==0 and (x[i]*x[i+1])%2!=0:
        kolvo+=1
        maximus=max(maximus,x[i]+x[i+1])
print(kolvo,maximus)
