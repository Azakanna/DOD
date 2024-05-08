g= ''
n = input()
for i in range (len(n)):
    if i % 3 != 0:
        g = g + n[i]
print(g)