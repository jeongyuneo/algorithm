n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
for i in range(n):
    idx = b.index(a[i])
    count = a[:i].count(a[i])
    print(idx+count, end=' ')