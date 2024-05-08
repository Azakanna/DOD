def f(n):
    counter=0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            counter+=1
            if n//i!=i:
                counter+=1
    return counter
kolvo=0
for i in range(123123,321322):
    if f(i)==3:
        kolvo+=1
print(kolvo)
