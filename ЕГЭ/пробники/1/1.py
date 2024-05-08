for n in range (1,10000):
    m = bin(n)[2:]
    if n%2==0:
        m=m+'01'
    else:
        m ='11'+m+'0'
    b=int(m,2)
    if b>1021:
        print(n)
        break
