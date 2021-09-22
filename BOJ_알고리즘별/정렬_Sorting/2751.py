import sys

n = int(input())
a = list(int(sys.stdin.readline()) for i in range(n))
a.sort()
for i in range(n):
    print(a[i])