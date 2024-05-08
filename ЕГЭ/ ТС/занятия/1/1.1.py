n=43*7**103-21*7**57+98
g=0
while n >0:
    s=n % 7
    g+=s
    n //=7
print (g)
