f = open(r"C:\Users\hhov0\Downloads\Задание_4_ДЗ__tcfz.txt")
s = f.readline()+'++'
kolvo = 0
maks = 0
for i in range(1, len(s) - 2, 2):
    if s[i] == s[i + 1]:
        kolvo += 1
        maks = max(maks, kolvo)
        if s[i] == s[i + 2]:
            kolvo = 0
    else:
        kolvo = 0
kolvo = 0
for i in range(0, len(s) - 2, 2):
    if s[i] == s[i + 1]:
        kolvo += 1
        maks = max(maks, kolvo)
        if s[i] == s[i + 2]:
            kolvo = 0
    else:
        kolvo = 0

print(maks * 2)
