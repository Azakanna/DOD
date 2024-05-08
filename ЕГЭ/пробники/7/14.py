aa=7**103+6*7**104-3*7**57+98

counter=0
while aa>0:
    b=aa%7
    counter+=b
    aa=aa//7
print(counter)


