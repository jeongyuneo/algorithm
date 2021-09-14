def searchHansu(n):
    cnt = 0
    if n < 10:
        cnt += int(n)
        return cnt
    elif n < 100:
        cnt += int(n)
    else:
        cnt += 99
        for i in range(100, int(n)+1):
            a, b, c = int(i/100), int((i%100)/10), int(i%10)
            if b - a == c - b:
                cnt += 1
    return cnt

n = int(input())
print(searchHansu(n))