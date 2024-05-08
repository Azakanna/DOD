def f(st,fin,cmd):
    if st==fin and cmd==7:
        return 1
    if cmd>7:
        return 0
    x=f(st+1,fin,cmd+1)
    y=f(st+4,fin,cmd+1)
    z=f(st*2,fin,cmd+1)
    return x+y+z
print(f(3,27,0))
