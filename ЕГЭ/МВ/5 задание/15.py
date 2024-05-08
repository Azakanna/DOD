counter=0
for i in range (100,1000):
    n=i
    a=sorted([int(x) for x in str(n)])
    x=int(str(a[2])+str(a[1]))
    y = int(str(a[0]) + str(a[1]))
    if x-y ==58:
        counter += 1
print(counter)
