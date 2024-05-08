def f(st,fin,cmd,flag11,flag13):
    if st==11:
        flag11=True
    if st==13:
        flag13=True
    if st==fin and cmd==9 and flag11==False and flag13==True:
        return 1
    if (st>fin) or (st==fin and cmd>9) or (st==fin and cmd==9 and flag11==True) and \
                (st==fin and cmd==9 and flag11==False and flag13==False):
        return 0

    x = f(st + 1, fin, cmd + 1, flag11, flag13)
    y = f(st + 3, fin, cmd + 1, flag11, flag13)
    z = f(st * 2, fin, cmd + 1, flag11, flag13)
    return x+y+z
print(f(1,18,0,False,False))