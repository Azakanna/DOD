f=open (r"C:\Users\hhov0\Downloads\Задание_17__rg3t.txt")
a=f.readlines()
b=[]
for i in a:
    b.append(int(i))
kolvo=0
maximus=-10000000
for i in range (0,len(b)-1):
    n=b[i]
    m=b[i+1]
    if (n+m)%2==0 and (n*m)%2==1:
        kolvo=kolvo+1
        if (n+m)>maximus:
            maximus=(n+m)
print(kolvo,maximus)
