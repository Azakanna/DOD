def f(n):
    simba = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            simba += i
            if n // i != i:
                simba += n // i
    return simba
cunter=0
for i in range(1,(10**6)+1):
    summadel=str(f(i))
    if len(summadel)>=3:
        if summadel[0]=='1' and summadel[-1]=='8' and summadel[-2]=='3':
            cunter+=1

print(cunter)