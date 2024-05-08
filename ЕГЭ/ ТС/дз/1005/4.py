f=open(r"C:\Users\hhov0\Downloads\4.txt")
s=f.readlines()
counter=0
for i in range(len(s)):
    a=s[i]
    if a.count('S')==a.count('X'):
        counter+=1
print(counter)