for n in range(1,9):
    r=bin(n)[2:]
    if n%2==0:
        a='10'+r
    else:
        a='1'+r+'01'
    b=int(a,2)
    print(b)