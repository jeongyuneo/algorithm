a = int(input())
b = list(map(int, input().split()))
M, m = b[0], b[0]
for i in range(1, a):
    if M < b[i]:
        M = b[i]
    if m > b[i]:
        m = b[i]
print(m, M)