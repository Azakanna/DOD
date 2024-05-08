def f(st,cmd):
    global b
    if cmd==13:
        b.add(st)
        return 1
    if cmd>13:
        return 0
    x=f(st+3,cmd+1)
    y=f(st*2+1,cmd+1)
    return x+y
b=set()
f(2,0)
print(len(b))
