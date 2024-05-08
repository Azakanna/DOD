a=25**20+4*5**11-2
counter=0
while a!=0:
    counter+=a%5==3
    a=a//5
print(counter)