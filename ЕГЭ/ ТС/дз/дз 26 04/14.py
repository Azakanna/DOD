def prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


counter = 0
summa = 0
for i in range(157314, 853413):
    if (int(i ** 0.5) == i ** 0.5) and prime(i ** 0.5):
        counter += 1
        summa += i
print(counter, summa)
