n = int(input())
cows = []
for i in range(n):
    cows.append(list(map(int, input().split())))
cows.sort(key=lambda x: (x[0], x[1]))
enter_time = 0
for i in range(n):
    if cows[i][0] > enter_time:
        enter_time = sum(cows[i])
    else:
        enter_time += cows[i][1]
print(enter_time)