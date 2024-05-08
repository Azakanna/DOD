for n in range (2,10000):
    r=bin(n)[2:]
    if r.count('1')>r.count('0'):
        r+='1'
    else:
        r+='0'
    if r.count('1') > r.count('0'):
            r += '1'
    else:
            r += '0'
    b=int(r,2)
    if b<99:
        print(int(r,2))