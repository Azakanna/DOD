# for n in range(1,256):
#     m=bin(n)[2:]
#     m='0'*(8-len(m))+m
#     l=m[:-1]
#     o=l[::-1]
#     u=int(o,2)
#     if u==n and u<100:
#         print(u)
#
#
#
# for n in range(1000,10000):
#     m=str(n)
#     x=m[0]
#     y=m[1]
#     z=m[2]
#     w=m[3]
#     xy=int(x)*int(y)
#     yz=int(y)*int(z)
#     zw=int(z)*int(w)
#     a=[xy,yz,zw]
#     a.sort()
#     h=str(a[1])
#     p=str(a[0])
#     if int(h+p)==1815:
#         print(n)



# for n in range(1,10000):
#     r=bin(n)[2:]
#     a=r.count('1')%2
#     r+=str(a)
#     a = r.count('1') % 2
#     r += str(a)
#     if int(r,2)>43:
#         print(r,int(r,2))

#
# for n in range(2,10000):
#     r=bin(n)[2:]
#     r=r[0:-1]+r[1]*2
#     if int(r,2)>92:
#         print(n)


# for n in range(10000,100000):
#     m=str(n)
#     q=(int(str(n)[0])**2)+(int(str(n)[2])**2)+(int(str(n)[4])**2)
#     w=(int(str(n)[1])**2)+(int(str(n)[3])**2)
#     minim=min(q,w)
#     maks=max(q,w)
#     i=str(maks)
#     l=str(minim)
#     if int(l+i)==2597:
#         print(n)

# f=open(r"C:\Users\hhov0\Downloads\2 (3).txt")
# n=[int(x) for x in f.readlines()]
# kolvo=0
# summa=0
# maks=0
# for i in range(len(n)-1):
#     x=n[i]
#     y=n[i+1]
#     p=str(x*y)
#     if p[-2] == '7':
#         kolvo+=1
#         summa=x+y
#         if summa %77==0:
#             maks=max(summa,maks)
# print(kolvo,maks)

f=open(r"C:\Users\hhov0\Downloads\3 (3).txt")
n=[int(x) for x in f.readlines()]
kolvo=0
maks=0
for i in range(len(n)-2):
    x=n[i]
    y=n[i+1]
    z=n[i+2]
    xx=bin(x)[2:]
    yy=bin(y)[2:]
    zz=bin(z)[2:]
    if (xx.count('1')>=3 and xx.count('0')>=1) + (yy.count('1')>=3 and yy.count('0')>=1) \
            + (zz.count('1')>=3 and zz.count('0')>=1)>=2:
        kolvo+=1
        maks=max(x,y,z,maks)
print(kolvo,maks)
















