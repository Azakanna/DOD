def f(st,fin,cmd,flag13):
    if st==13:
        flag13=True
    if cmd==9 and st==fin and flag13==True:
        return 1
    if (cmd<9 and st==fin) or cmd>9 or flag13==False and st==fin or st>fin or st==11:
        return 0
    x=f(st+3,fin,cmd+1,flag13)
    y=f(st+1,fin,cmd+1,flag13)
    z=f(st+st,fin,cmd+1,flag13)
    return x+y+z
print(f(1,28,0,False))