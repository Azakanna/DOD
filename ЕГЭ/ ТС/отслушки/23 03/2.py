def f(n):
    if n ==1:
        return 1
    if n % 2 ==0 and n > 1:
        return 2 *n *f(n - 1)
    if n>1 and n % 2 != 0:
        return n + f(n - 2)
print(f(50))
