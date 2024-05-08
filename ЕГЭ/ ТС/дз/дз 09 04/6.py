def f(st,cmd,mas):
    if cmd>7:
        return 0
    if cmd == 7:
        if not (st in mas):
            mas.append(st)
        return 1
    x = f(st * 2, cmd + 1, mas)
    y = f(st * 2 + 1, cmd + 1, mas)
    z = f(st * 3 + 1, cmd + 1, mas)
    return x+y+z
b=[]
f(1,0,b)
print(len(b))

