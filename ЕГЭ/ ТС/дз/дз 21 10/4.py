from functools import cache


def moves(h):
    a, b = h
    return (a * 5, b), (a, b * 5), (a + 4, b), (a, b + 4)


@cache
def f(h):
    if sum(h) >= 287:
        return 'END'
    if all(f(x) == 'END' for x in moves(h)):
        return 'WIN1'
    if any(f(x) == 'WIN1' for x in moves(h)):
        return 'LOSE1'



for i in range(1, 264):
    n=i,23
    print(i,f(n))
