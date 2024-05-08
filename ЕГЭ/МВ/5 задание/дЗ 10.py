for n in range(1000,10000):
    r=str(n)
    a=(int(r[0]))*(int(r[1]))
    b=(int(r[1]))*(int(r[2]))
    c=(int(r[2]))*(int(r[3]))
    x,y=max(a,b,c),min(a,b,c)
    s=sum([a,b,c])
    pred=s-x-y
    v=str(pred)+str(y)
    if v=='1816':
        print(n)



#9928

