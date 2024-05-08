counter=0
x=25
for i in range(1,int(x**0.5)+1):
    if x%i==0:
        counter+=1
        if x//i!=i:
            counter+=1
    # if i**2==x:
    #     counter-=1
print(counter)