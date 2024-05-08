# f=open(r"C:\Users\hhov0\Downloads\24_1 (1).txt")
# s=f.readlines()
# z=sorted('QWERTYUIOPASDFGHJKLZXCVBNM')
# a=[0]*26
# maximus=0
# o=''
# for i in range(len(s)):
#     u=s[i]
#     kolvo=0
#     for l in range(len(u)-1):
#         if ord(u[l])== ord(u[l+1])-1:
#             kolvo+=1
#     if kolvo>maximus:
#         maximus=kolvo
#         o=u
# for p in range(len(z)):
#     a[p]=o.count(z[p])
# t=max(a)
# for g in range(len(z)):
#     if a[g]==t:
#         print(z[g])

def prime(n):
    kolvo = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

kolvo = 0

for p in range(2, 98):

    if prime(p)==True:
        m = p ** 4
        if 22_222_222 <= m <= 88_888_888:
            kolvo+=1
            print(m,p)
print(kolvo)
