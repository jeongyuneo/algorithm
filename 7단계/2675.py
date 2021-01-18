n = int(input())
for i in range(n):
    a, b = map(str, input().split())
    tmp = ''
    for i in range(len(b)):
        for j in range(int(a)):
            tmp += b[i]
    print(tmp)