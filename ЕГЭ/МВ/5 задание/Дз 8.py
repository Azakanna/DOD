for n in range (10000,100000):
    r=str(n)
    a=int(r[0])+int(r[1])
    b=int(r[2])+int(r[3])
    c=int(r[0])+int(r[4])
    minim=min(a,b,c)
    s=sum([a,b,c])-minim-max(a,b,c)
    if str(minim)+str(s)=='311':
        print(n)
        break
