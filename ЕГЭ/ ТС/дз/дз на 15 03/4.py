# def f(a,b,c):
#     if (a**2==b**2+c**2) or (b**2==a**2+c**2) or (c**2==a**2+b**2):
#         print(True)
#     else:
#         print(False)
# f(20,19,1)

def f (a,b,c):
    if (a+b>c) and ( a + c > b) and (c + b > a):
        return True
    else:
        return False
print(f(20,19,1))


