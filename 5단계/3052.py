a = list(int(input()) for i in range(10))
b = list(a[i] % 42 for i in range(10))
cnt = 0
for i in range(42):
    if i in b:
        cnt += 1
print(cnt)