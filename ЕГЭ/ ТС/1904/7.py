from functools import cache
def moves(h):
    a,b=h
    return (a+2,b),(a,b+2),(a*3,b),(a,b*3)
@cache
def f(h):
    if sum(h)>=59:
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
    h=5,i
    print(i,f(h))