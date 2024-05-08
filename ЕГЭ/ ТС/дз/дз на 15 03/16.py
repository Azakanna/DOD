n = input()
if n.count('f') == 1:
    print(-1)
elif n.count('f') == 0:
    print(-2)
else:
    s = (n.find('f' , n.find('f') + 1))
    print(s)



