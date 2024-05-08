from fnmatch import *
for x in range(0,10**6,7):
    if fnmatch(str(x),'2738*'):
        print(x,x//7)