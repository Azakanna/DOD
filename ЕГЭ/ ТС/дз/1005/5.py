f=open(r"C:\Users\hhov0\Downloads\5.txt")
s=f.readlines()
counter=0
for i in range(len(s)):
    a=s[i]
    if a.count('A')>a.count('S'):
        counter+=1
print(counter)