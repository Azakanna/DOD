def f(st,fin,flag11):
    if st==11:
        flag11=True
    if flag11==True and st==fin:
        return 1
    if st>fin or flag11==False and st==fin or st==13 or st==18:
        return 0
    x=f(st+4,fin,flag11)
    y=f(st+5,fin,flag11)
    z=f(st*2,fin,flag11)
    return x+y+z
print(f(3,23,False))