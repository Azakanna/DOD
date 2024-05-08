# from functools import  cache
# @cache
# def f(st,fin,cmd,flag10):
#     if st==15:
#         flag10= True
#     if st==fin and flag10= True  and cmd
a=[0]*1000
a[2]=1
for i in range(3,16):
    a[i] = a[i-1]+a[i-2]
    if i%3==0:
        a[i] += a[i//3]
    if i ==10:
        for j in range (1,i):
            a[j] = 0
    if i==14:
        a[i]=0
print(a[15])
