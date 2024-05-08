def f(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 3
    if n>3:
        return f(n-3)+g(n-3)+2
def g(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n>2:
        return g(n-1)+f(n-1)
print(f(9))

