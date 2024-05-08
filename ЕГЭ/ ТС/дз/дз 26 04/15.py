from fnmatch import *


def f(n):
    simba = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            simba += i
            if n // i != i:
                simba += n // i
    return simba


counter = 0
for i in range(12306540, 12396550):
    if (fnmatch(str(i), '123?654?')):
        if f(i) > i:
            counter += 1

print(counter)
