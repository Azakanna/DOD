# def f(st,fin,cmd):
#     if st==fin  and cmd == 25:
#         return  1
#     if cmd > 25:
#         return 0
#     if st%2==0:
#         x=f(st//2,fin,cmd+1)
#     y=f(st+1,fin,cmd+1)
#     if st%3==0:
#         b=st//3
#     z=f(st+b,fin,cmd)
#     return x+y+
from functools import cache
@cache
def f(st,fin,cmd):
    if st==fin and cmd == 25:
        return  1
    if cmd>25:
        return 0
    x=f(st//2,fin,cmd+1)*(st%2==0)
    y=f(st+1,fin,cmd+1)
    z=f(st+st//3,fin,cmd+1)*(st%3==0)
    return x+y+z
print(f(1,60,0))