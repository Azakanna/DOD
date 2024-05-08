#рекурсивная функция для n числа фибаначаи
def feb(n):
    if n in (1 , 2):
        return 1
    return feb(n - 1) + feb( n - 2)
print(feb(7))


a = 1
b = 1
n = int(input())
summ = 0
min = 0
while min < n - 2:
    summ = a+b
    a=b
    b=summ
    min = min + 1
print(b)


#арифм прогрессия
def r(a,k,n):
    if n == 1:
        return a
    return  k + r ( a , k , n - 1 )
print(r(1,2,5))


def f(n):
    if n < 4:
        return 2 ** n
    if n > 3 and (n%2) == 0:
        return 2 * f (n-1) + f(n//2)
    if n > 3 and (n%2) == 1:
        return  f(n-2) + 1**n + f(n//5)
print(f())














