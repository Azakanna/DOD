def prime(n):
    if n == 1:
        return False
    for i in range(2, int(n * 0.5) + 1):
        if n % i == 0:
            return False
    return True


cunter = 0
for i in range(56846, 59034):
    if prime(i) == True:
        cunter += 1
print(cunter)
