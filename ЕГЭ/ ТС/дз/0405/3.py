a=4**19+2**8+31
counter=0
while a!=0:
    counter+=a%2==1
    a=a//2
print(counter)