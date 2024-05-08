for n in range(1,1000):
    r=bin(n)[2:]
    if n%2==0:
        e='1'+str(r)+'1'
    else:
        e='1'+str(r)+'01'
    u=int(e,2)
    if u>420:
        print(n)
        