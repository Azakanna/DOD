a = [0] * 20
a[2] = 1
for i in range (3,16):
    a[i] += a[i - 1] + a[i-2]
    if  i % 3 == 0 :
        a[i] += a[i//3]
    if i == 10:
        for j in range(10):
            a[j] = 0
    if i == 14:
        a[i] = 0
print(a[15])
