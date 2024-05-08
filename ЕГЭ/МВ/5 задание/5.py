for n in range (1,100000):
    r=bin(n)[2:]
    r+=r[-1]
    if r.count('1')%2==0:
        r+='0'
    else:
        r+='1'
    if r.count('1') % 2 == 0:
            r += '0'
    else:
            r += '1'
    b=int(r,2)
    if b > 120:
        print(n)
        break

