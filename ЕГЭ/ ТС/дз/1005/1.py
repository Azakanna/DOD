f=open(r"C:\Users\hhov0\Downloads\1.txt")
s=f.readline()
maks=0
counter=0
for i in range(len(s)):
    if s[i]=='V':
        counter+=1
        if counter>maks:
            maks=counter
    else:
        counter=0
print(maks)

# f=open(r"C:\Users\hhov0\Downloads\1.txt")
# s = f.readline()
# counter=0
# while 'V' in s:
#     counter+=1
# print(counter)