f=open(r"C:\Users\hhov0\Downloads\17_1.txt")
a=f.readlines()
b=[]
for i in a:
    b.append(int(i))
kolvo=0
minim=10000000000
for i in range (0,len(b)-1):
    n=b[i]
    m=b[i+1]
    if n*m>0 and (n+m)%7==0:
        kolvo=kolvo+1
        if n*m<minim:
            minim=n*m
print(kolvo,minim)