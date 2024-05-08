for n in range (1000,10000):
    r=str(n)
    a=int(r[0])+int(r[1])
    b=int(r[1])+int(r[2])
    c=int(r[2])+int(r[3])
    z=sorted([a,b,c])
    v=str(z[-1])+str(z[-2])
    if v=='1412':
        print(n)
        break
