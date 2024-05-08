# s=open(r"C:\Users\hhov0\Downloads\24_17.txt").readlines()
# kolvo=0
# mi=''
# minim=10**8
# for i in range(len(s)):
#     s[i]=s[i][:-1]
#     if len(s[i])<minim:
#         minim=len(s[i])
#         mi=s[i]
# for l in range (minim//2):
#     if mi[l]==mi[len(mi)-1-l]:
#         kolvo+=1
# print(kolvo)

# s = open(r"C:\Users\hhov0\Downloads\24_18.txt").readlines()
# nom=0
# maks=-10**8
# si=''
# for i in range(len(s)):
#     si=s[i]
#     counter = 1
#     for l in range(len(si)-1):
#         if si[l]=='W' and si[l+1]=='W':
#             counter+=1
#             if counter > maks:
#                 nom = i + 1
#                 maks = counter
#         else:
#             counter=1
# print(nom)











