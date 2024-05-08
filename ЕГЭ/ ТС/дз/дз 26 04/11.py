def f(n):
    counter=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            counter+=1
            if n//i!=i:
                counter+=1
    return counter

for i in range(5000000,9999,-1):
    if f(i)==10:

        print(i)
        break
