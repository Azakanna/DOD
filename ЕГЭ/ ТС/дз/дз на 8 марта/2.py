f=open(r"C:\Users\hhov0\Downloads\17_2.txt")
a=f.readlines()
b=[]
for i in a:
    b.append(int(i))
kolvo=0
maxim=-100000
for i in range (0,len(b)-2):
    n=b[i]
    m=b[i+1]
    v=b[i+2]
    flag1=n%3==0 or m%3==0 or v%3==0
    flag2=(n+m+v)%2==0
    flag3=((n+m+v)/3)<m
    if flag1 and flag2 and flag3:
        kolvo=kolvo+1
        if n+m+v>maxim:
            maxim=n+m+v
print(kolvo,maxim)