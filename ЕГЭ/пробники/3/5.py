for n in range(2,10000):
    r=bin(n)[2:]
    b=str(r)
    k=b[:-1]+b[1]+b[1]
    h=int(k,2)
    if h>115:
        print(n)
        break


