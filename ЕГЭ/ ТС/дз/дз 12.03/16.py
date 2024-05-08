n=int(input())
sum=n
count=0
for i in range(1, n):
    sum+=i
    count+= int(input())
print(sum-count)