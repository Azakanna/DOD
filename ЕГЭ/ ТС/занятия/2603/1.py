from functools import cache
def moves(h):
   a,b = h
   return (a + 3,b),(a,b + 3),(a * 2,b),(a,b * 2)

@cache
def f(h):
    if sum(h) >= 31:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'WIN1'
    if all(f(x) == 'WIN1' for x in moves(h)):
        return  'LOSE1'
    if any(f(x) == 'LOSE1' for x in moves(h)):
        return 'WIN2'
    if all(f(x) == 'WIN1' or f(x) == 'WIN2' for x in moves(h)):
        return 'LOSE2'

for S in range(1,26):
    h = 4,S
    print(S,f(h))
