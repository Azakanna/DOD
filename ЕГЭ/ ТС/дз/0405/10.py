def summa(n):
    kolvo=0
    while n>0:
        kolvo+=n%10
        n=n//10
    return kolvo
def delit(n):
    kolvoo=0
    for l in range(2,int(n**0.5)+1):
        if n%l==0:
            kolvoo+=1
            if n//l!=l:
                kolvoo+=1
    return kolvoo
counter=0
SUMMA=0
for i in range(51232,421422):
    if (i%summa(i)==0) and (delit(i)==6):
        counter+=1
        SUMMA+=i
p=SUMMA//counter
print(counter,p)

