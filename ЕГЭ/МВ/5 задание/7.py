for n in range(1,10000):
    r=bin(n)[2:]
    if (n%2==0):
        r+='11'
    else:
        r+='00'
    x=int(r,2)-(len(bin(n)[2:]))
    if x==126:
        print(n)
        break