for x in range (0,100):
    n= '1678012'
    m= '10024'
    a=int(n,16)
    b=int(m,16)
    k=a+x*(16**2)
    l=b+x*(16**3)
    if (k+l)%15==0:
        print(x)
        break