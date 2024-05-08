n=(66+6**2019)*6**2019+66+6**6
gg=0
while n > 0:
    s=n % 6
    gg+=s
    n//=6
print(gg)