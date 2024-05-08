# counter=0
# def f(n):
#     kol=0
#     m=int(n**0.5)
#     for i in range(2,m+1):
#         if m//i!=0:
#             kol+=i
#             if m//i!=i:
#                 k=n//i
#                 kol+=k
#     return  kol
# p='0123456789'
# for x in p:
#     for y in p:
#         kol='123'+x+'654'+y
#         n=int(kol)
#         if f(n)>n:
#             counter+=1
# print(counter)
