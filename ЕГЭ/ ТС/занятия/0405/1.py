# f=open(r'C:\Users\hhov0\Downloads\24_1.txt')
# s=f.readline()
# a=s.count('AR')
# b=s.count('AM')
# summa=a+b
# print(summa)

# f=open(r'C:\Users\hhov0\Downloads\24_2.txt')
# counter=0
# s=f.readline()
# for i in range(len(s)-1):
#     if s[i]=='B' and s[i+1]=='A':
#         counter+=1
# print(counter)

# f=open(r'C:\Users\hhov0\Downloads\24_3.txt')
# maks=0
# counter=0
# s=f.readline()
# for i in range(len(s)):
#     if s[i]=='B':
#         counter+=1
#         if counter>maks:
#             maks=counter
#     else:
#         counter=0
# print(maks)

# f=open(r'C:\Users\hhov0\Downloads\24_4.txt')
# maks=0
# counter=1
# s=f.readline()
# for i in range(len(s)-1):
#     if s[i]!=s[i+1]:
#         counter+=1
#         if counter>maks:
#             maks=counter
#     else:
#         counter=1
# print(maks)

# f=open(r'C:\Users\hhov0\Downloads\24_5.txt')
# counter=0
# s=f.readline()
# print(s[0])
# for i in range(len(s)-1):
#     if (s[i]=='T' and s[i+1]=='O' and s[i+2]=='K') and s[i-1]!='S':
#         counter+=1
# print(counter)

# f = open(r'C:\Users\hhov0\Downloads\24_6.txt')
# counter=0
# maks=0
# chetko='DSMREAIK'
# s=f.readline()
# for i in range(len(s)):
#     if s[i] in chetko:
#         counter+=1
#         if counter>maks:
#             maks=counter
#     else:
#         counter=0
# print(maks)

# f = open(r'C:\Users\hhov0\Downloads\24_7.txt')
# counter=0
# a=f.readlines()
# for i in range(len(a)):
#     s=a[i]
#     if s.count('S')==s.count('X'):
#         counter+=1
# print(counter)

# f = open(r'C:\Users\hhov0\Downloads\24_8.txt')
# counter=1
# maks=0
# gl='AEIOUY'
# s=f.readline()
# for i in range(len(s)-1):
#     if (s[i] in gl) and not(s[i+1] in gl) or not(s[i] in gl) and (s[i+1] in gl):
#         counter+=1
#         if counter>maks:
#             maks=counter
#     else:
#         counter=1
# print(maks)

# f = open(r'C:\Users\hhov0\Downloads\24_9.txt')
# s=f.readline()
# spisok=sorted('QWERTYUIOPASDFGHJKLZXCVBNM')
# a=[0]*26
# for i in range(26):
#     a[i]=s.count(spisok[i])
# maximusubica=max(a)
# for x in range(26):
#     if a[x]==maximusubica:
#         print(spisok[x])

# f = open(r'C:\Users\hhov0\Downloads\24_10.txt')
# s=f.readline()
# s=s.replace('MS','M*S')
# s=s.replace('SM','S*M')
# a=s.split('*')
# maximus=-10**8
# for i in range(len(a)):
#     if len(a[i])>maximus:
#         maximus=len(a[i])
# print(maximus)













