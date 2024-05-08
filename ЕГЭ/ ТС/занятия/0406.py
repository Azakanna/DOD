# f=open(r"C:\Users\hhov0\Downloads\1 (5).txt")
# s=f.readline()
# maks=0
# kolvo=1
# for i in range(0,len(s)-2,2):
#     if s[i]=='B' and s[i+2]=='B':
#         kolvo+=1
#         maks=max(kolvo,maks)
#     else:
#         kolvo=1
# kolvo=1
# for i in range(1,len(s)-2,2):
#     if s[i]=='B' and s[i+2]=='B':
#         kolvo+=1
#         maks=max(kolvo,maks)
#     else:
#         kolvo=1
# print(maks)


# f=open(r"C:\Users\hhov0\Downloads\2 (4).txt")
# s=f.readline()
# s=s.replace('OSR','*')
# s=s.replace('RSO','*')
# maks=0
# kolvo=1
# for i in range(len(s)-1):
#     if s[i]=='*' and s[i+1]=='*':
#         kolvo+=1
#         maks=max(kolvo,maks)
#     else:
#         kolvo=1
# print(maks*3)


# f=open(r"C:\Users\hhov0\Downloads\3 (4).txt")
# s=f.readline()
# a=[0]*26
# alp=sorted('QWERTYUIOPASDFGHJKLZXCVBNM')
# maks=0
# kolvo=0
# for i in range(len(s)):
#     if s[i]=='Y':
#         for l in range(26):
#             if s[i+1]==alp[l]:
#                 a[l]+=1
# for q in range(26):
#     if a[q]==max(a):
#         print(alp[q])


# f=open(r"C:\Users\hhov0\Downloads\4 (3).txt")
# s=f.readline()
# maks=0
# kolvo=0
# a=[]
# for i in range(1,len(s)-1):
#     if s[i-1]<s[i]>s[i+1]:
#         a.append(i)
# for l in range(len(a)-1):
#     maks=max(maks,a[l+1]-a[l])
# print(maks)
#
# ------------------------------------------------------------------------------
# def dels(n):
#     a=[]
#     for i in range(1,int(n**0.5)+1):
#         if n%i==0:
#             a.append(i)
#             l=n//i
#             if n%l==0:
#                 if l!=i:
#                     a.append(l)
#     return a
# kolvo=0
# summa=0
# for i in range(8_214,342_142):
#     if len(dels(i))%2==0 and len(dels(i))%3==0:
#         kolvo+=1
#         summa+=i
# print(kolvo,summa)

#
# def prime(n):
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# kolvo=0
# for i in range(8_214,342_142):
#     if prime(i)==True:
#         kolvo+=1
# print(kolvo)



# def dels(n):
#     a=[]
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             a.append(i)
#             l=n//i
#             if l!=i:
#                 a.append(l)
#     return a
# def prime(n):
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return  True
# kolvo=0
# maks=0
# for i in range(12_524,15_422):
#     dl=dels(i)
#     flag = True
#     for l in range(len(dl)):
#         if prime(dl[l])==False:
#             flag=False
#     if flag==True:
#         kolvo+=1
#         maks=max(maks,i)
# print(kolvo,maks)


# def dels(n):
#     a=[]
#     for i in range(1,int(n**0.5)+1):
#         if n%i==0:
#             l = n // i
#             if i%2==0:
#                 a.append(i)
#             if l!=i and l%2==0:
#                 a.append(l)
#     return a
# kolvo=0
# summa=0
# for i in range(88_535,167_043):
#     if len(dels(i))==5:
#         kolvo+=1
#         summa+=i
# srarf=summa//kolvo
# print(kolvo,srarf)

# from math import sqrt
# def prime(n):
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return  True
# kolvo=0
# summa=0
# a=sqrt(853412)
# for i in range(int(a)+1):
#     if prime(i)==True:
#         l=i**2
#         if 157_314<l<853_412:
#             kolvo+=1
#             summa+=l
# print(kolvo,summa)

from math import sqrt
def prime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
kolvo=0
a=sqrt(sqrt(10**10))
for i in range(int(a)+1):
    if prime(i)==True:
        for k in range(100):
            l=i**4*2**k
            if 10**6<l<10**10:
                kolvo+=1
print(kolvo)
















