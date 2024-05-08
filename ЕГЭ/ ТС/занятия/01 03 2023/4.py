#ВВОДИТ ЧИСЛО N ПОТОМ ВВОДИТ N ЧИСЕЛ ВЫВОДИТ КОЛВО ЧИСЕЛ КОТОРЫЕ БОЛЬШЕ 15
n=int(input())
kolvo=0

for i in range(n):
    x=int(input())
    if x > 15:
        kolvo+=1
print(kolvo)

