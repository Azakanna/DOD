f = open(r"C:\Users\hhov0\Downloads\17.txt")
s = [int(x) for x in f]
kolvo = 0
maks = 0
for i in range(len(s) - 2):
    q = bin(s[i])[2::]
    w = bin(s[i + 1])[2::]
    e = bin(s[i + 2])[2::]
    q1 = (q.count('1') >= 3) * (q.count('0') >= 1)
    w1 = (w.count('1') >= 3) * (w.count('0') >= 1)
    e1 = (e.count('1') >= 3) * (e.count('0') >= 1)
    if sum([q1, w1, e1]) >= 2:
        kolvo += 1
        maks = max(maks, s[i], s[i + 1], s[i + 2])
print(kolvo, maks)
