x=1052336
a=[1,2,98,43,89,739]
counter=0
for i in a:
    if x%i==0:
        counter+=x//i
print(counter)