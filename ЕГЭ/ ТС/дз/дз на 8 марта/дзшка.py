
for x in range(4):
    a = (int('1' + str(x) + '34', 6) + int('23' + str(x) + '1', 4))
    if a % 7 == 0:
        print(a//7)