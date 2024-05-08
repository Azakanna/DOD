a=7**103+6*7**104-3*7**57+98
counter=0
while a>0:
    b=a%7
    counter+=b
    a=a//7
print(counter)
