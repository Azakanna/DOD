mas = []
for a in range(10):
    s = '78' + str(a) + '56321'
    if int(s) % 279 == 0:
        mas.append(int(s))
    for b in range(1, 10, 2):
        s = '78' + str(a) + '56' + str(b) + '321'
        if int(s) % 279 == 0:
            mas.append(int(s))
    for c in range(1, 10, 2):
        for d in range(1, 10, 2):
            s = '78' + str(a) + '56' + str(c) + str(d) + '321'
            if int(s) % 279 == 0:
                mas.append(int(s))
    for c in range(1, 10, 2):
        for d in range(1, 10, 2):
            for e in range(1, 10, 2):
                s = '78' + str(a) + '56' + str(c) + str(d) + str(e) + '321'
                if int(s) % 279 == 0:
                    mas.append(int(s))
mas.sort()
for x in range(len(mas)):
    y = mas[x] // 279
    print(mas[x], y)
