for n in range(1000):
    r=bin(n)[2:]
    r=r+r[-1]
    if r.count('1')%2==0:
        r=r+'0'
    else:
        r=r+'1'
    if r.count('1')%2==0:
        r=r+'0'
    else:
        r=r+'1'
    u=int(r,2)
    if u>136:
        print(n)
        break