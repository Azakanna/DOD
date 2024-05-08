from fnmatch import *
for x in range(0,10**10,1017):
    if fnmatch(str(x),'2?5432*1'):
        print(x,x//1017)