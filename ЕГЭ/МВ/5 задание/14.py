for n in range (1,10000):
    r=bin(n)[2:]
    if (r.count('1')%2==0):
        r='10'+r[2:]+'0'
    else:
        r='11'+r[2:]+'1'
    v=int(r,2)
    if v>40:
        print(n)
        break
