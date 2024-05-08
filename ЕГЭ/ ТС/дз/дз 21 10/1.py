from functools import cache

def moves(h):
    return (h + 1), (h * 2)

@cache
def f(h):
    if h >= 25:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'WIN1'
    if all(f(x) == 'WIN1' for x in moves(h)):
        return 'LOSE1'
    if any(f(x) == 'LOSE1' for x in moves(h)):
        return 'WIN2'
    if all(f(x) == 'WIN1' or f(x) =='WIN2' for x in moves(h)):
        return 'LOSE2'

for i in range(1, 25):
    if f(i) == 'LOSE2':
        print(i)

