def f(n):
    kolvo = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i==0:
            l = n // i
            if i % 17 == 0:
                kolvo += 1
            if l % 17 == 0 and l != i:
                kolvo += 1
    if kolvo == 3:
        return True
    else:
        return False


def dels(n):
    a = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.append(i)
            l = n // i
            if l != i:
                a.append(l)
    return sorted(a)


for i in range(750000, 930000 + 1):
    if f(i) == True:
        h=dels(i)
        print(i,h[0],h[1],h[2])
