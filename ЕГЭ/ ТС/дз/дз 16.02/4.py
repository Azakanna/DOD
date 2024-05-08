n=int(input())
a=[]
b=[]
for i in range(n):
    x=int(input())
    if x > 7:
        a.append(x)
    if x<=7:
        b.append(x)
print(a,b)
