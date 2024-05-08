a = [0] * 1000
a[1] = 1
for i in range(2,15):
    a[i] += a[i-1] + a[i-2]
    if i == 8:
        a[i] = 0
print(a[14])