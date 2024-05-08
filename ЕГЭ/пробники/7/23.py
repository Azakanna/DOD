def f(st,fin,flag15,flag12):
    if st==15:
        flag15=True
    if st==12:
        flag12=True
    if st==fin and  flag15==True and flag12==False:
        return 1
    if st>fin or st==fin and flag12==True:
        return 0
    x=f(st+1,fin,flag15,flag12)
    y=f(st+3,fin,flag15,flag12)
    return x+y
print(f(5,25,False,False))