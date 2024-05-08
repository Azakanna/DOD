def f(st,cmd,nechet):
    global b
    if cmd>10:
        return 0
    if st%2==1:
        nechet+=1
    if nechet>3:
        return 0
    if cmd==10 and nechet<=3:
        b.add(st)
        return 1
    x = f(st +1, cmd + 1,nechet)
    y = f(st +3, cmd + 1,nechet)
    z = f(st * 3, cmd + 1,nechet)
b= set()
f(2,0,0)
print(len(b))



