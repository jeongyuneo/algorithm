import sys

n = int(sys.stdin.readline())
a = list(set(map(int, sys.stdin.readline().rsplit(' '))))
a.sort()
for i in a:
    print(i, end=' ')