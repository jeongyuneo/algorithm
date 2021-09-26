import sys

a = sys.stdin.readline().rstrip()
b = list(a[i:] for i in range(len(a)))
b.sort()
for i in b:
    print(i)