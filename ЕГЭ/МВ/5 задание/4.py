for n in range (765,10000):
    r=bin(n)[2:]
    r=str(int(r[::-1]))
    if int(r,2)==23:
        print(n)
        break