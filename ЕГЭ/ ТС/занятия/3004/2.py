def f8(n):
    s = ''
    while n > 0:
        s = str(n % 8) + s
        n = n // 8
    return s


f = open(r'C:\Users\hhov0\Downloads\17__wlh5.txt')
a = [int(t) for t in f]
kolvo = 0
maximus = -10 ** 9
minim = 10 ** 9
bol = -100000000000
for i in range(len(a)):
    if a[i] % 127 == 0 and a[i] > bol:
        bol = a[i]
for i in range(len(a) - 1):
    if a[i] > bol or a[i + 1] > bol:
        x = f8(a[i])
        y = f8(a[i + 1])
        if x.count('31') > 0 or y.count('31') > 0:
            kolvo += 1
            if a[i] + a[i + 1] < minim:
                minim = a[i] + a[i + 1]
print(kolvo, minim)
