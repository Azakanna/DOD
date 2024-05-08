def f(x):
    d=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
def s(x):
    k=0
    a=x
    while a>0:
        k+=a%10
        a=a//10
    if x%k==0:
        return True
otv=[]
otv2=0
for x in range(51242,421422):
    d=f(x)
    if len(d)==6 and s(x):
        otv.append(x)
        otv2+=x
print(len(otv),otv2//len(otv))