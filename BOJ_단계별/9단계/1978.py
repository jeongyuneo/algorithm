n = int(input())
l = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if l[i] == 1:
        continue
    j = 2
    while j <= l[i]:
        if j == l[i]:
            cnt += 1
        if l[i] % j == 0:
            break
        j += 1
print(cnt)