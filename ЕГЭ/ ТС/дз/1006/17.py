def f(st,fin):
    if st==fin:
        return True
    if st<fin:
        return False
    x=f(st-1,fin)
    y=f(st-3,fin)
    z=f(st//3,fin)
    return x+y+z
print(f(22,2))