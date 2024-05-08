f=open(r"C:\Users\hhov0\Downloads\17__13m6t.txt")
b=2686
a=[int(f.readline()) for i in range(b)]
d=sum(a)
g=len(a)
srarf=d/g
kolvo=0
p= -100000000
for i in range (b-1):
    x=a[i]
    y=a[i+1]
    if x>srarf or y > srarf:
        if abs(x)%10==6 or abs(y)%10==6:
            kolvo+=1
            p=max(p,x+y)
print(kolvo,p)