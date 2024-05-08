f = open(r"C:\Users\hhov0\Downloads\26_2.txt")
n, m = map(int, f.readline().split())
a = []
for i in range(m):
    x, y = map(int, f.readline().split())
    a.append([x, i, y])
a.sort()
kolvo = 0
minim = 0
baza = [-1] * n
for i in range(m):
    flag = False
    if a[i][0] > 1440:
        break
    for l in range(n):
        if a[i][0] >= baza[l]:
            baza[l] = a[i][2] + a[i][0]
            kolvo += 1
            if kolvo == 1591:
                print(l + 1)
            flag = True
            break
    if flag == False:
        minim = min(baza)
        if minim >= 1440:
            break
        for l in range(n):
            if baza[l] == minim:
                baza[l] += a[i][2]
                kolvo += 1
                if kolvo == 1591:
                    print(l + 1)
                break

print(kolvo)
