n = input()
n = n.replace('h', 'H', n.count('h') - 1)
n = n.replace('H', 'h', 1)
print(n)