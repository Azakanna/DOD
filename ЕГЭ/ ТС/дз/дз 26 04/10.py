def f(n):
    counter=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            counter+=1
            if n//i!=i:
                counter+=1
    return counter
otvet=0
for i in range(421431,754124):
    if f(i)==12:
        otvet+=1
print(otvet)

