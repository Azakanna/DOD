
def f(num):
    n = str(num)
    summ=0
    for i in range(len(n)):
        summ = summ + int(n[i])
    return summ



def fun(num):
    summ = 0
    while num > 0:
        summ = summ + (num % 10)
        num = num // 10
    return summ
print(fun(42893589), f(42893589) )