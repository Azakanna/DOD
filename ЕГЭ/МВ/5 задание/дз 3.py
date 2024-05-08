for n in range(10000):
    r=bin(n)[2:]
    r=r+r[-1]
    if r.count('1')%2==0:
        r=r+'0'
    else:
        r=r+'1'
    if r.count('1') % 2 == 0:
         r = r + '0'
    else:
         r = r + '1'
    v=int(r,2)
    if v>90:
        print(n)
        break


