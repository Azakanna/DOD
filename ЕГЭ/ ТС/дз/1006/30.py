for  n in range(1,1000):
    if n%4!=0:
        r=hex(n//2)[2:]
        r='F'+r+'A0'
    if n%4==0:
        r=hex(n//2)[2:]
        r='15' + r+'C'
    if int(r,16)<1048576:
        print(n)