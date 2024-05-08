for n in range (2,100000):
    r=bin(n)[2:]
    r+=r[1]
    r += r[-2]
    b=int(r,2)
    if b<90:
        print(n)
