for n in range (1,200):
    r=bin(n)[2:]
    r+=str(r.count('1')%2)
    r += str(r.count('1') % 2)
    if int(r,2)>166:
        print(int(r,2))
        break
        
