def f(st,fin):
    if st==fin:
        return 1
    if st>fin:
        return 0
    x,y,z=0,0,0
    if st!=0 and st!=1:
        x=f(st**2,fin)
    if st!=0 and st>0:
        y=f(st*2,fin)
    z=f(st+3,fin)
    return x+y+z
counter=0
for st in range(-20,21):
    counter+=f(st,20)
print(counter)