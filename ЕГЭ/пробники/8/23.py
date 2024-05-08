def f(st,fin):
    if st==fin:
        return  1
    if int(st)>int(fin):
        return 0
    x=f(bin(int(st,2)+1)[2:],fin)
    y=f('1'+st,fin)
    return x+y
print((f('1','11111')))