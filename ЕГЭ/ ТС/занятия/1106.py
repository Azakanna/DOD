# def f(n):
#     if n%4==0:
#         return True
#     else:
#         return False
# file=open(r"C:\Users\hhov0\Downloads\27_1.txt")
# n=int(file.readline())
# a=[int(x) for x in file.readlines()]
# maks=0
# for i in range(len(a)):
#     for l in range(i+1,len(a)):
#         x=a[i]
#         y=a[l]
#         if f(x)==True and f(y)==True:
#             p=x*y
#             maks=max(maks,p)
# print(maks)

# def f(n,m):
#     if (n+m)%8==0:
#         if (n*m)%5==0:
#             return True
#     else:
#         return False
# file=open(r"C:\Users\hhov0\Downloads\27_2.txt")
# n=int(file.readline())
# a=[int(x) for x in file.readlines()]
# kolvo=0
# for i in range(len(a)):
#     for l in range(i+1,len(a)):
#         x=a[i]
#         y=a[l]
#         if f(x,y)==True:
#             kolvo+=1
# print(kolvo)
#
# def f(n,m):
#     if ((n+m)%91==0) and (n>33 or m>33):
#         return True
#     else:
#         return False
# file=open(r"C:\Users\hhov0\Downloads\27_3.txt")
# n=int(file.readline())
# a=[int(x) for x in file.readlines()]
# kolvo=0
# for i in range(len(a)):
#     for l in range(i+1,len(a)):
#         x=a[i]
#         y=a[l]
#         if f(x,y)==True:
#             kolvo+=1
# print(kolvo)

# def f(n,m):
#     if ((n+m)%11==0):
#         return True
#     else:
#         return False
# file=open(r"C:\Users\hhov0\Downloads\27_4.txt")
# n=int(file.readline())
# a=[int(x) for x in file.readlines()]
# minim=10**8
# summa=0
# for i in range(len(a)):
#     for l in range(i+3,len(a)):
#         x=a[i]
#         y=a[l]
#         if f(x,y)==True:
#             summa+=x+y
#             minim=min(minim,x+y)
# print(minim,summa)

# def f(n):
#     if n%2==0:
#         return False
#     else:
#         return True
# file=open(r"C:\Users\hhov0\Downloads\27_5.txt")
# n=int(file.readline())
# a=[int(x) for x in file.readlines()]
# k=10
# maks=-10**8
#
# for i in range(len(a)):
#     for l in range(i,len(a)):
#         summa=0
#         kk=0
#         for t in range(i,l+1):
#             summa+=a[t]
#             if f(a[t])==True:
#                 kk+=1
#         if kk%10==0:
#             if summa>maks:
#                 maks=summa
# print(maks)
# #
#
# f=open(r"C:\Users\hhov0\Downloads\27_6.txt")
# n=int(f.readline())
# a=[int(x) for x in f.readlines()]
# dl=0
# maks=-10**8
# for i in range(len(a)):
#     for l in range(i,len(a)):
#         summa = 0
#         for t in range(i,l+1):
#             summa+=a[t]
#             if summa%751==0 and summa>maks:
#                 dl=l-i+1
#                 maks=summa
#                 ATVETJIEST=maks*dl
# print(ATVETJIEST)
# #
#
#
#
# f=open(r"C:\Users\hhov0\Downloads\27_7.txt")
# n=int(f.readline())
# a=[int(x) for x in f.readlines()]
# maks=-10**8
# otvet=0
# for i in range(len(a)):
#     for l in range(i,len(a)):
#         summa=0
#         for t in range(i,l+1):
#             summa+=a[t]
#             if summa%21==0 and summa>maks:
#                 maks=summa
#                 otvet=maks-(1+l-i)
# print(otvet)
#
#
#

















































