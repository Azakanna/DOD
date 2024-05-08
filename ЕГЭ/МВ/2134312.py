# # # # while True: print(eval(input('>>>')))
# # # a='32222'
# # # b=int(a,4)
# # #
# # # print(b)
# # a=10001
# # b=bin(a)[2:]
# # print(b)
# def check(A):
#     for x in range(1,1000):
#         f=(x&25!=0) <= ((x&17==0) <= (x&A!=0))
#         if f==False:
#             return False
#     return True
# for A in range(1000):
#     if check(A)==True:
#         print(A)
#         break
def check(a):
    for x in range(1,1000):
        f=(x&144==0)<=((x&220!=0)<=(x&a!=0))
        if f == False:
            return False
    return True
for a in range(1000):
    if check(a) == True:
        print(a)
        break