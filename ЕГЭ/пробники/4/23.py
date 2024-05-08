def f(st,fin):
    if st<fin:
        return 0
    if st==fin:
        return 1
    x=f(st-1,fin)
    y=f(st//2,fin)
    return x+y
print(f(20,1))