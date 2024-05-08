from functools import cache
def moves(h):
    o=[]
    if h%2==0:
        o+= [h//2]
    else:
        if h>1:
            o+=[h-2]
    if h%3==0:
        o+=[h-(h*2/3)]
    else:
        if h>2:
            o+=[h-3]
    return o
@cache
def f(h):
    if h<=2:
        return 'end'
    if any(f(x) == 'end' for x in moves(h)):
        return 'win1'
    if all(f(x) == 'win1' for x in moves(h)):
        return 'lose1'
    if any(f(x)=='lose1' for x in moves(h)):
        return 'win2'
    if all(f(x)=='win1' or f(x)=='win2' for x in moves(h)):
        return 'lose2'

for i in range (1,100):
    h=i
    print(i,f(h))