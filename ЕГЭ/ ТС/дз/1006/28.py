otv=0
for i in range(1,10):
    s=str(i)+'1231'
    if int(s)%11==0:
        otv+=1
    for l in range(10):
        s1=str(i)+'123'+str(l)+'1'
        if int(s1)%11==0:
            otv+=1
    for l in range(10):
        for p in range(10):
            s2=str(i)+'123'+str(l)+str(p)+'1'
            if int(s2)%11==0:
                otv+=1
print(otv)