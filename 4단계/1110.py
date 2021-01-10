a = int(input())
tmp = a
new = 0
cnt = 0
while True:
    l = []
    if tmp < 10:
        l.append(0)
        l.append(tmp)
    else:
        l.append(int(tmp / 10))
        l.append(int(tmp % 10))
    tmp = l[0] + l[1]
    new = l[1] * 10 + tmp % 10
    tmp = new
    cnt += 1
    if a == new:
        break
print(cnt)