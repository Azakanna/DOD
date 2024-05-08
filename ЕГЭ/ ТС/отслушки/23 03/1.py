def f(n):
    if n== 1:
        return 0
    if n in [2,3]:
        return 1
    else:
        return f(n - 1) +f(n - 2)
print(f(11))
