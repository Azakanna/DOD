def f(x):
    d=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return  sorted(d)
a=[]
for x in range(2,1000):
    d=f(x)
    if d==[]:
        a.append(x)
for n in range(1,6):
    s='>'+'1'*n+'2'*39+'0'*39
    while '>1' in s or '>2' in s or '>0'in s:
        if '>1' in s:
            s=s.replace('>1','22>',1)
        if '>2' in s:
            s=s.replace('>2','2>',1)
        if '>0' in s:
            s=s.replace('>0','1>',1)
    summa=s.count('1')+s.count('2')*2
    if summa in a:
        print(n)