s = open(r"C:\Users\hhov0\Downloads\9.txt").readline()
flag = False
ans = 0
counter = 0
for i in range(len(s)):
    if s[i] == 'R':
        flag = False
    if s[i] == 'A' and flag == True:
        counter += 1
        if counter >= 15:
            ans += 1
        counter = 1

    elif s[i] == 'A':
        counter = 1
        flag = True
    else:
        counter += 1

print(ans)

# s = f.readline()
# start = s[0]
# end = s[-1]
# counter = 0
# s = s.split('A')
# if start != 'A':
#     s.pop(0)
# if end != 'A':
#     s.pop(-1)
# for i in range(len(s)):
#     if len(s[i]) >= 13:
#         if 'R' not in s[i]:
#             counter += 1
# print(counter)
