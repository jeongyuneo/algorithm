a = int(input())
for i in range(a):
    b = list(map(int, input().split()))
    s = 0
    for j in range(1, b[0]+1):
        s += b[j]
    avg = s / b[0]
    c = 0
    for j in range(1, b[0]+1):
        if b[j] > avg:
            c += 1
    print('%0.3f%%'%(c / b[0] * 100))