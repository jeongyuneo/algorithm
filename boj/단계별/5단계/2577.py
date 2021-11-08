a = list(int(input()) for i in range(3))
b = list(0 for i in range(10))
tmp = str(a[0] * a[1] * a[2])
for i in range(len(b)):
    b[i] = tmp.count(str(i))
for i in range(len(b)):
    print(b[i])