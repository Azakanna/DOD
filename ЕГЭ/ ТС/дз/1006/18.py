def f(st,fin,flag8):

    if st==8:
        flag8=True
    if st==fin and flag8==False:
        return True
    if st>fin or st==fin and flag8==True:
        return False
    x=f(st+1,fin,flag8)
    y=f(st+2,fin,flag8)
    z=f(st*2,fin,flag8)
    return x+y+z
print(f(3,13,False))