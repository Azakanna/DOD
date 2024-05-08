def f(n):
    r=bin(n)[2:]
    if r.count('1')==3:
        return True
    else:
        return False
file=open(r"C:\Users\hhov0\Downloads\17_t.txt")
n=[int(x) for x in file]
summa=0
kolvo=0
for i in range(len(n)-2):
    if f(n[i])==True and f(n[i+1])==True and f(n[i+2])==True:
        p=max(n[i],n[i+1],n[i+2])
        summa+=p
        kolvo+=1
print(kolvo,summa)


def f(st,fin,cmd,flag22):
    if st==22:
        flag22=True
    if st==fin and cmd==12 and flag22==False:
        return 1
    if (st>fin) or (st==fin and cmd>12) or (st==fin and cmd==12 and flag22==True):
        return 0
    x,y,z=0,0,0
    if st%3==0:
        x=f(st+2,fin,cmd+1,flag22)
    if st%2==0:
        y=f(st+3,fin,cmd+1,flag22)
    if st%3!=0 and st%2!=0:
        z=f(st+1,fin,cmd+1,flag22)
    return x+y+z
print(f(3,27,0,False))
from functools import lru_cache
def moves(h):
    a,b=h
    return (a+2,b),(a,b+2),(a*3,b),(a,b*3)
@lru_cache(None)
def f(h):
    if sum(h)>=59:
        return 'END'
    if any(f(x)=='END' for x in moves(h)):
        return 'WIN1'
    if all(f(x)=='WIN1' for x in moves(h)):
        return 'LOSE1'
    if any(f(x)=='LOSE1' for x in moves(h)):
        return 'WIN2'
    if all(f(x)=='WIN2' or f(x)=='WIN1' for x in moves(h)):
        return 'LOSE2'
for s in range(1,54):
    h=5,s
    if f(h)=='LOSE2':
        print(s)
        break


перевод в  любую сс
n-число в 10сс , m-в какую сс хотим
def ss_univerasl(n,m):
    alp='0123456789ABCDEF'
    s=''
    while n>0:
        ost=n%m
        s=alp[ost]+s
        n=n//m
    return s


def ss_prostoi(n):       #для примера на 7
    s=''
    while n>0:
        s=str(n % 7)+s
        n=n//7
    return s



#проверка на прОстоту
def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

#нахождение делителей
def deli(n):
    a=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            a.append(i)
            l=n//i
            if i!=l:
                a.append(l)
    return sorted(a)


# 8 НОМЕР ПРОГОЙ каждая буква скок угодно раз
a = 'ВАСИЛ'  # ВАСИЛИСА
gl = 'АИ'
sgl = 'ВСЛ'
otv = 0

for x in a:
    for y in a:
        for z in a:
            for w in a:
                for q in a:
                    for r in a:
                        slovo = x + y + z + w + q + r
                        kolvo = 0  # gl
                        counter = 0  # sogl
                        for i in range(len(slovo)):

                            if slovo[i] in gl:
                                kolvo += 1
                            if slovo[i] in sgl:
                                counter += 1

                        if kolvo > counter:
                            otv += 1
print(otv)


# 8 НОМЕР ПРОГОЙ с перестановкой букв
a='МАРИНА'
gl='АИ'
sgl='МРН'
b=set()
for x in sgl:
    for y in a:
        for z in a:
            for w in a:
                for q in a:
                    for r in a:
                        slovo = x + y + z + w + q + r
                        flag=True
                        for i in a:
                            if a.count(i)!=slovo.count(i):
                                flag=False
                        if flag==True:
                            b.add(slovo)
print(len(b))



#6 номера синтексис

from turtle import *
m=15  #маштаб
tracer(0)   #трасер
up() / down()   #поднять опусмтить хвост
for x in range (-50,50):   #сетка по Х
    for y in range(-50,50):   # сетка по Y
        goto(x*m,y*m)    # Движение по сетке
        dot(5, 'Purple')    # точки на сетке
update()       # обновление сетки
exitonclick()   # чтобы не выключалось после завершения


#26 полезные штуки
x, y = map(int, f.readline().split())   # читать цифры с файла переводя сразу в инт в переменные
a.append([x,i, y])    # добавить в массив значения времени
a.sort()   # отсортировать по живой очереди



# 23 пример решения с флагами
def f(st,fin,cmd,flag22):
    if st==22:
        flag22=True
    if st==fin and cmd==12 and flag22==False:
        return 1
    if (st>fin) or (st==fin and cmd>12) or (st==fin and cmd==12 and flag22==True):
        return 0
    x,y,z=0,0,0
    if st%3==0:
        x=f(st+2,fin,cmd+1,flag22)
    if st%2==0:
        y=f(st+3,fin,cmd+1,flag22)
    if st%3!=0 and st%2!=0:
        z=f(st+1,fin,cmd+1,flag22)
    return x+y+z
print(f(3,27,0,False))

# 19-21 синтексис + пример решения

from functools import lru_cache
def moves(h):
    a,b=h
    return (a+2,b),(a,b+2),(a*3,b),(a,b*3)
@lru_cache(None)
def f(h):
    if sum(h)>=59:
        return 'END'
    if any(f(x)=='END' for x in moves(h)):
        return 'WIN1'
    if all(f(x)=='WIN1' for x in moves(h)):
        return 'LOSE1'
    if any(f(x)=='LOSE1' for x in moves(h)):
        return 'WIN2'
    if all(f(x)=='WIN2' or f(x)=='WIN1' for x in moves(h)):
        return 'LOSE2'
for s in range(1,54):
    h=5,s
    if f(h)=='LOSE2':
        print(s)
        break

5 номер срезы
у среза есть 3 параметра 1 ( ниже цифра 1)    параметр начало 2 (ниже цифра 2) параметр конец 3 шаг (ниже цифра -1)
a[1:2:-1]
c помощью шага -1 можно перевернуть число ил можно задать параметр шага 2 для того чтобы бегать по четным или нечетным значениям числа

12 номер
самое важное не забыть что реплейс присваивается
пример
a=a.replace('1','2',1)
у реплейса 3 параметра 1 параметр что заменяем , 2 параметр на что заменяем и 3 параметр сколько раз заменяем


f=open(r"C:\Users\hhov0\Downloads\26__1jacu.txt")
n=int(f.readline())
a=[int(x) for x in f.readlines()]
a.sort(reverse=True)
kor=[a[0]]
for i in range(n):
    if kor[-1] - a[i] >=3:
        kor.append(a[i])
        dlina=len(kor)
        u=kor[-1]
print(dlina,u)

f=open(r"C:\Users\hhov0\Downloads\26__1j92j (1).txt")
n=int(f.readline())
a=sorted([int(x) for x in f],reverse=True)
otv=1
x=a[0]
for i in range(1,len(a)):
    if (x-a[i])>=5:
        otv+=1
        x=a[i]
print(otv,x)


















































