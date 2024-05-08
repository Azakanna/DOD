# как было написано
for c in range(3):
    s = '12' + str(c)
for d in range(3):
    for e in range(3):
        s = '12' + str(c) + str(d)
        print(s, end=' ')

print()

# как стало написано
for c in range(3):
    s = '12' + str(c)
for d in range(3):
    for e in range(3):
        s = '12' + str(d) + str(e)
        print(s, end=' ')

