# f=open(r'C:\Users\hhov0\Downloads\24_11.txt')
# s=f.readline()
# summ=0
# kolvo=0
# for i in range(0,len(s),2):
#     summ+=int(s[i])
#     kolvo+=1
# print(summ,kolvo,summ/kolvo)

# f=open(r'C:\Users\hhov0\Downloads\24_12.txt')
# s=f.readline()
# ans=int(s[0])
# for i in range(2,len(s),2):
#     if s[i-1]=='-':
#         ans-=int(s[i])
#     else:
#         ans+=int(s[i])
# print(ans)

# f=open(r'C:\Users\hhov0\Downloads\24_13.txt')
# s=f.readline()
# kolvo=0
# for i in range(len(s)-1):
#     if s[i]==s[i+1]:
#         kolvo+=1
# print(kolvo)

# f=open(r'C:\Users\hhov0\Downloads\24_14.txt')
# s=f.readline()
# maks=0
# counter=0
# for i in range(len(s)):
#     if s[i]!='R' or s[i]=='R' and s[i+1]!='R':
#         counter+=1
#         maks=max(maks,counter)
#     if s[i]=='R' and s[i+1]=='R':
#         counter=counter+1
#         maks=max(maks,counter)
#         counter=0
# print(maks)

# f=open(r'C:\Users\hhov0\Downloads\24_15.txt')
# s=f.readline()
# maks=5
# counter=5
# for i in range(len(s)-5):
#     if s[i]!=s[i+3] or s[i+1]!=s[i+4] or s[i+2]!=s[i+5]:
#         counter+=1
#         maks = max(maks, counter)
#     else:
#         counter=5
# print(maks)

# f=open(r'C:\Users\hhov0\Downloads\24_16.txt')
# s=f.readline()+'='
# maks=0
# counter=0
# for i in range(1,len(s)-1,2):
#     if s[i]==s[i+1]:
#         counter+=2
#         maks = max(maks, counter)
#         if s[i+2]==s[i+1]:
#             counter=0
#     else:
#         counter=0
# counter=0
# for i in range(0,len(s)-1,2):
#     if s[i]==s[i+1]:
#         counter+=2
#         maks = max(maks, counter)
#         if s[i+2]==s[i+1]:
#             counter=0
#     else:
#         counter=0
# print(maks)
#
