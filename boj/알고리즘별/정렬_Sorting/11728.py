n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.extend(b)
for x in sorted(a):
    print(x, end=' ')