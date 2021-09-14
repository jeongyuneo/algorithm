a = list(int(input()) for _ in range(9))
M = a[0]
num = 1
for i in range(1, len(a)):
    if M < a[i]:
        M = a[i]
        num = i + 1
print('%d\n%d'%(M, num))