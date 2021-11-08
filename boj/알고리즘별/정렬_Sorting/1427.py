import sys

n = str(sys.stdin.readline())
a = list(n[i] for i in range(len(n)-1))
a.sort()
a.reverse()
b = ''
for i in range(len(a)):
    b += a[i]
print(int(b))