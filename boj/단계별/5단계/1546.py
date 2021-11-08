a = int(input())
b = list(map(int, input().split()))
maxB = max(b)
s = 0
for i in range(len(b)):
    s += b[i] / maxB * 100
print(s / a)