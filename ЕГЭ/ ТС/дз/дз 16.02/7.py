a=[0,1,2,3,4,5,6,7,8,9]
for i in range(0,len(a)):
    for j in range (i+1,len(a)):
        for h in range(j+1,len(a)):
            print(a[i],a[j],a[h])