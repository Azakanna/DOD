def f(st,fin):
    if st>fin:
        return 0
    if st==fin:
        return 1
    return f(st+1,fin)+f(st+10,fin)
print(f(12,36))