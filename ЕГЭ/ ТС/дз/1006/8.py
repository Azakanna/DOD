a=(66+6**2019)*6**2019+66+6**6
counter=0
while a>0:
    b=a%6
    counter+=b
    a=a//6
print(counter)