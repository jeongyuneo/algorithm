import sys

n = int(input())
a = []
for i in range(n):
    b, c = map(int, sys.stdin.readline().split(' '))
    a.append([b, c])
a.sort()
for i in range(n):
    for j in range(2):
        print(a[i][j], end=' ')
    print()