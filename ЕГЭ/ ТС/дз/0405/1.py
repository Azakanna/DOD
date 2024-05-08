a=5**14+25**3-117
counter=0
while a!=0:

    counter+=a%5==4
    a=a//5
print(counter)