def f(x,y):
    if x==y:
        return 1
    if y>x:
        return 0
    if x>1:
        return f(x//2,y)+f(x-1,y)
print(f(64,14))

