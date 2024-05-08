def f(st,fin,cmd,flag15):
    if st==15:
        flag15=True
    if st == fin and cmd == 20 and flag15==True:
        return 1
    if st==fin and flag15==False or cmd>20 or st>fin or st==fin and cmd<20:
        return 0
    x=f(st+1,fin,cmd+1,flag15)
    y=f(st*2,fin,cmd+1,flag15)
    if st%8==0:
        z=f(st+st*0.75,fin,cmd+1,flag15)
    else:
        z=0
    return x+y+z
print(f(3,50,0,False))




