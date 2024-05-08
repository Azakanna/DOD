f = open(r"C:\Users\hhov0\Downloads\26_1.txt")
k = 210
n = 987
a = []
maks=0
for i in range(n):
    x, y = map(int, f.readline().split())
    maks=max(maks,y)
    a.append([x, i, y])
a.sort()
storage = [-1] * k
kolvo=0
for i in range(n):
    for l in range(k):
        if a[i][0]>=storage[l]:
            storage[l]=a[i][2]+1
            kolvo+=1
            if kolvo==340:

            break
print(kolvo)