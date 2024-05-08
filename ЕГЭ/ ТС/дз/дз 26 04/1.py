counter=0
from fnmatch import *
for x in range(0,10**6,5):
    if fnmatch(str(x),'8?321?'):
        counter+=1
        print(counter)