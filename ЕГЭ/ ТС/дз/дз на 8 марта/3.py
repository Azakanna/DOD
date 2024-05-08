f=open(r"C:\Users\hhov0\Downloads\17_3.txt")
a=f.readlines()
b=[]
for i in a:
    b.append(int(i))
kolvo=0
min=10000000
for i in range (0,len(b)-1):
    n=b[i]
    m=b[i+1]
    if (n <60  and m <60) and (n%5==0 or n%8==0 or m%5==0  or m%8==0):
        kolvo=kolvo+1
        if n+m<min:
            min=n+m
print(kolvo,min)
