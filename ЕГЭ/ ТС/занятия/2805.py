# f=open(r"C:\Users\hhov0\Downloads\6_2.txt")
# n=int(f.readline())
# a=[[0]*10001 for i in range(10001)]
# ryad=0
# maks=0
# for l in range(n):
#     x,y=map(int,f.readline().split())
#     a[x][y]=1
# for j in range(10001):
#     counter=1
#     for q in range(len(a[j])-1):
#         if a[j][q]==1 and a[j][q+1]==1:
#             counter+=1
#             if counter>maks:
#                 maks=max(counter,maks)
#                 ryad=j
#         else:
#             counter=1
# print(maks,ryad)





f=open(r"C:\Users\hhov0\Downloads\5_1.txt")
s=f.readline().split()
kolvo=int(s[0])
pod=int(s[1])

a=[]
for i in  range(kolvo):
    x=int(f.readline())
    if x<200 or x>210:
        a.append(x)
    else:
        pod=pod-x
print(pod)