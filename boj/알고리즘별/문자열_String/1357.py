def Rev(x):
    x = str(x)
    result = ''
    for i in range(len(x)-1, -1, -1):
        result += x[i]
    return int(result)

a, b = map(int, input().split(' '))
print(Rev(Rev(a)+Rev(b)))