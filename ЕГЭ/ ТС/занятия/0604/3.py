def f(st,fin,cmd):
    if st == fin and cmd==12:
        return 1
    if st>fin or cmd>12 or st == 22:
        return 0
    x,y,z=0,0,0
    if st % 3 == 0:
        x = f(st+2,fin,cmd+1)
    if st %2==0:
        y = f(st+3,fin,cmd+1)
    if st%2!=0 and st%3!=0:
        z = f(st+1,fin,cmd+1)
    return x +y + z
print(f(3,27,0))
