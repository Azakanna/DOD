from functools import cache
def moves(h):
    a,b,c=h
    o=[]
    if a>1:
        o+=[((a + 1) // 2, b, c)]
        o+=[(a-1,b,c)]
    if b>1:
        o+=[(a,(b+1)//2,c)]
        o+=[(a,b-1,c)]
    if c>1:
        o+=[(a,b,(c+1)//2)]
        o+=[(a,b,c-1)]
    return o
@cache
def f(h):
    if sum(h)<=32:
        return 'end'
    if any(f(x) == 'end' for x in moves(h)):
        return 'win1'
    if all(f(x) == 'win1' for x in moves(h)):
        return 'lose1'
    if any(f(x)=='lose1' for x in moves(h)):
        return 'win2'
    if all(f(x)=='win1' or f(x)=='win2' for x in moves(h)):
        return 'lose2'


for i in range (1,54):
    h=11,11,i
    print(i,f(h))