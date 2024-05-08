mas = []
for a in range(10):
    s = '12345' + str(a) + '67'
    if int(s) % 257 == 0:
        mas.append(int(s))
    for b in range(0, 10, 2):
        s = '123'+str(b)+'45'+str(a)+'67'
        if int(s) % 257 == 0:
            mas.append(int(s))
    for c in range(0, 10, 2):
        for d in range(0, 10, 2):
            s = '123'+str(c)+str(d)+'45'+str(a)+'67'
            if int(s) % 257 == 0:
                mas.append(int(s))
    for c in range(0, 10, 2):
        for d in range(0, 10, 2):
            for e in range(0, 10, 2):
                s = '123'+str(c)+str(d)+str(e)+'45'+str(a)+'67'
                if int(s) % 257 == 0:
                    mas.append(int(s))
mas.sort()
for x in range(len(mas)):
    y = mas[x] // 257
    print(mas[x], y)
