def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return  True
def dels(m):
    a=[]
    for i in range(2,int(m**0.5)+1):
        if m%i==0:
            if prime(i)==True:
                a.append(i)
            l=m//i
            if prime(l)==True:
                if l!=i:
                    a.append(l)
    return sorted(a)[::-1]
for i in range(100_000,500_001):
    a=dels(i)
    if len(a)>3:
        raz=(max(a)-min(a))//(len(a)-1)
        flag=True
        for l in range(len(a)-1):
            if a[l]-a[l+1]!=raz:
                flag=False
        if flag==True:
            print(i,len(a)*raz)




