n=int(input())
kolvo=0
summ=0
for i in range(n):
    x=int(input())
    if x>15 and x%3==0:
        kolvo= kolvo+1
    if x%7==3:
        summ= summ+x
print (kolvo,summ)
