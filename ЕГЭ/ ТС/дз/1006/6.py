a=64**10+2**90-16
counter=0
while a!=0:
    b=a%8
    if b==7:
        counter+=1
    a=a//8
print(counter)

