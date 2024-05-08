n=str(643)
m=int(n,7)
a=str(432)
b=int(a,7)
q=m+b
counter=0
while q>0:
    j=q % 3
    if j == 1:
        counter +=1
    q//=3
print(counter)