a = int(input())
cnt = 1
tmp = 1
n = 1
while True:
    if a == 1:
        break
    n += 6 * tmp
    cnt += 1
    if a > n:
        tmp += 1
    else:
        break
print(cnt)
