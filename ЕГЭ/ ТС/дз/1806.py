f = open(r"C:\Users\hhov0\Downloads\26__1ux2w.txt")
k = 210
n = 600
a = []
for i in range(n):
    x, y = map(int, f.readline().split())
    a.append([x, y])
a.sort()
kolvo = 0
storage = [-1] * k
for i in range(n):
    for l in range(k):
        if a[i][0] >= storage[l]:
            storage[l] = a[i][1] + 1
            kolvo += 1
            if kolvo == 492:
                u=l+1
            break
print(kolvo,u)
























# f=open(r"C:\Users\hhov0\Downloads\26__1j92j.txt")
# n=int(f.readline())
# a=sorted([int(x) for x in f],reverse=True)
# kol=1
# x=a[0]
# for i in range(1,len(a)):
#     if (x-a[i])>=5:
#         kol+=1
#         x=a[i]
# print(kol,x)










































# for i in range(n):
#     flag=False
#     if a[i][0]>1440:
#         break
#     for l in range(n):
#         if a[i][0]>=storage[l]:
#             storage[l]=a[i][2]+a[i][0]
#             kolvo+=1
# print(kolvo)
