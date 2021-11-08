a = int(input())
for i in range(a):
    s = input()
    score = 0
    tmp = 1
    for j in s:
        if j == 'O':
            score += tmp
            tmp += 1
        else:
            tmp = 1
    print(score)