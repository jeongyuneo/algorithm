import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().rsplit()))
a.sort()
cnt = 0
i, j = 0, n-1
while i < j:
    if a[i] + a[j] == m:
        cnt += 1
        i += 1
        j -= 1
    elif a[i] + a[j] < m:
        i += 1
    else:
        j -= 1
print(cnt)