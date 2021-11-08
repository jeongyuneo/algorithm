n = int(input())
a = list(map(int, input().split(' ')))
a.sort()
s = 0
cnt = 1
for i in range(n):
    for j in range(cnt):
        s += a[j]
    cnt += 1
print(s)