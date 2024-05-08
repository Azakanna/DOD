f = open(r'C:\Users\hhov0\Downloads\dz17-27__tcdi.txt')
a = [int(x) for x in f]
kolvo = 0
maxim = -10 ** 9
mimim = 10**9
bol = 0
for i in range(len(a)):
    if a[i] > bol and a[i] % 131 == 0:
        bol = a[i]
for i in range(len(a)-1):
    if a[i] > bol or a[i + 1] > bol:
        if str(a[i]).count('11') > 0 or str(a[i + 1]).count('11') > 0:
            kolvo += 1
            if a[i] + a[i + 1] < mimim:
                mimim = a[i] + a[i + 1]
print(kolvo,mimim)