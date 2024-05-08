# a=int(input())
# b=int(input())
# c=int(input())
# if a>b>c or c>b>a:
#     print(b)
# if b>a>c or c>a>b:
#     print(a)
# if a>c>b or b>c>a:
#     print(c)
def f(a,b,c):
    x=0
    if a > b > c or c > b > a:
        x=b
    if b>a>c or c>a>b:
        x=a
    if a>c>b or b>c>a:
        x=c
    return x
print(f(12,5,17))