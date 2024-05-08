from fnmatch import *
for x in range(0,10**8,141):
    if fnmatch(str(x),'12*4?65'):
        print(x,x//141)