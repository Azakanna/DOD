for n in range (10000):
    r=bin(n)[2:]
    if n%2==0:
        r+= '11'
    else:
        r+= '00'
    v=int(r,2)
    x=v-len(bin(n)[2:])
    if x==126:
        print(n)
        break

