import sys

n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split(' '))))
a.sort(key=lambda x: (x[1], x[0]))
for x, y in a:
    print(x, y)