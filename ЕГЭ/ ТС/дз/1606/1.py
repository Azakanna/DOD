f=open(r"C:\Users\hhov0\Downloads\17_1 (3).txt")
n=[int(x) for x in f]
a=[]
for i in range(len(n)):
    if abs(n[i])%100==68:
        a.append(n[i])
mim=min(a)**2
k=m=0
for i in range(len(n)-1):
    if ((abs(n[i])%100==68 and abs(n[i+1])%100!=68) \
            or (abs(n[i])%100!=68 and abs(n[i+1])%100==68))\
            and ((n[i])**2+(n[i+1])**2)>=mim:
        k+=1
        m=max((n[i])**2+(n[i+1])**2,m)
print(k,m)










# # a='12345'
# # print(a[-2::])
# n=str([int(i) for i in f])
# minim=0
# kolvo=0
# maks=0
# for i in range(len(n)):
#     if str(n[i][-2::])=='68':
#         minim=min(minim,n[i])
# minim=minim**2
# for i in range(len(n)-1):
#     x=str(n[i])
#     y=str(n[i+1])
#     summa=int(x)**2 + int(y)**2
#     if summa>minim:
#         if ((n[i][-2::]=='68') and (n[i+1][-2::] != '68')) or \
#                 ((n[i][-2::] != '68') and (n[i + 1][-2::] == '68')):
#             kolvo+=1
#             maks=max(maks,summa)
# print(maks,p)
