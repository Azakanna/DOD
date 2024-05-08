f = open(r'C:\Users\hhov0\Downloads\17_2 (1).txt')
a = [int(x) for x in f]
kolvo = 0
maks = -10 ** 8
for i in range(len(a) - 1):
    p = a[i] * a[i + 1]
    if p > 10:
        o = str(p)
        if o[1] == '4':
            kolvo += 1
            if ((a[i] + a[i + 1])%24==0) and (a[i] + a[i + 1]) > maks:
                maks = a[i] + a[i + 1]
print(kolvo + maks)
