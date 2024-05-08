def f(st,fin,flag10,flag14):

    if st==10:
        flag10=True
    if st==14:
        flag14=True
    if st==fin and flag10==True and flag14==False:
        return True
    if st>fin or st==fin and flag10==False or st==fin and flag10==True and flag14==True:
        return False
    x=f(st+1,fin,flag10,flag14)
    y=f(st+2,fin,flag10,flag14)
    z=f(st*3,fin,flag10,flag14)
    return x+y+z
print(f(2,15,False,False))