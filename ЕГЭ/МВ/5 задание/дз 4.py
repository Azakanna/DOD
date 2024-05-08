for n in range (1000):
    r=bin(n)[2:]
    if r.count('1')%2==0:
        r+= '0'
    else:
        r+= '1'
    if r.count('1')%2==0:
        r+= '0'
    else:
        r+= '1'
    v=int(r,2)
    if v>150:
        print(v)
        break