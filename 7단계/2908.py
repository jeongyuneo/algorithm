a, b = map(str, input().split())
n1, n2 = 0, 0
for i in range(3):
    n1 += int(a[i]) * pow(10, i)
    n2 += int(b[i]) * pow(10, i)

if n1 > n2:
    print(n1)
else:
    print(n2)