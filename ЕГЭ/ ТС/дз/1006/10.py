def f(n):
    if n<3:
        return 2*n*n+2
    return f(n-1)+g(n-2)
def g(n):
    if n<3:
        return  2*n*n+2
    return g(n-2)+n*n-3
ff=f(15)
gg=g(5)
reportles=ff*gg
print(ff,gg,reportles)