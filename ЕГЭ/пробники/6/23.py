def f(st,fin):
    if st>fin:
        return 0
    if st==fin:
        return 1
    x=f(st+2,fin)
    y=f(st*4,fin)
    z=f(st+1,fin)
    return x+y+z
print(f(2,25))