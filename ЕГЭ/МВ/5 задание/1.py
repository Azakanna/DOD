for n in range (1,100000):
    r=bin(n)[2:]
    r+=str(r.count('1')%2)
    r+=str(r.count('1')%2)
    if int(r,2) > 100:
        print(int(r,2))
        break
