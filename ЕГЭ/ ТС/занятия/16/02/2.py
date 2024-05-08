f= open (r"C:\Users\hhov0\Downloads\17__ktcw__t5nl.txt")
a= f.readlines()
b= []
for i in a:
    b.append(int(i))
kolvo=0
maximus=-10000
for i in range (len(a)-1):
    n=b[i]
    m=b[i+1]
    if (n+m)%6==0 and (n+m)%9!=0 and (n+m)%10==2:
        kolvo=kolvo+1
    if (n*m)%10==7:
        if n*m>maximus:
            maximus=m*n
print(kolvo,maximus)

