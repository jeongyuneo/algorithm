import sys

n = int(input())
a = list(0 for i in range(10001))
while n > 0:
    b = int(sys.stdin.readline())
    a[b] += 1
    n -= 1
for i in range(1, 10001):
    for j in range(a[i]):
        print(i)