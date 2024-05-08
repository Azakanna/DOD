for n in range (10000):
    r=bin(n)[2:]
    if n%2==0:
        r+= '11'
    else:
        r+= '01'
    v=int(r,2)
    if v<128:
        print(v)



