def summ(n):
    summa=0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            summa+=i
            if n//i!=i:
                summa+=n//i
    return summa
def kolvo(n):
    kolvoo=0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            kolvoo+=1
            if n//i!=i:
                kolvoo+=1
    return kolvoo
for i in range(398790,863778):
    if summ(i)>2700000:
        print('Я крутой')
        print(kolvo(i),summ(i))