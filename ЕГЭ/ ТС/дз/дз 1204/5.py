def f(st,cmd):
    global b
    if cmd>10:
        return 0
    if cmd==10:
        b.add(st)
        return 1
    x,y,z=0,0,0
    if st>0 and st<10:
        x=f(st-10,cmd+1)
    if st!=0:
        y=f(st*(-2),cmd+1)
    if st<0:
        z=f(abs(st),cmd+1)
    return x+y+z
b=set()
f(1,0)
print(len(b))
