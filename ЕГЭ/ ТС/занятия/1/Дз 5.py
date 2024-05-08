q=343**5+7**3-1
for x in range (100000):
    counter=0
    p=q-x
    while p>0:
        o=p%7
        if o==6:
            counter+=1
        p//=7
    if counter==12:
        print(x)
        break
