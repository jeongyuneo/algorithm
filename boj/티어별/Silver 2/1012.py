count = int(input())
for i in range(count):
    res = 1
    m, n, k = map(int, input().split())
    location = []
    for j in range(k):
        a, b = map(int, input().split())
        location.append([a, b])
    v1, v2 = location[0][0], location[0][1]
    while len(location) > 0:
        if [v1, v2] in location:
            location.remove([v1, v2])
        if v1 - 1 >= 0 and [v1-1, v2] in location:
            location.remove([v1-1, v2])
            v1-= 1
            # print(1, v1, v2, location)
            continue
        if v2 - 1 >= 0 and [v1, v2-1] in location:
            location.remove([v1, v2-1])
            v2 -= 1
            # print(2, v1, v2, location)
            continue
        if v1 + 1 < m and [v1+1, v2] in location:
            location.remove([v1+1, v2])
            v1 += 1
            # print(3, v1, v2, location)
            continue
        if v2 + 1 < n and [v1, v2+1] in location:
            location.remove([v1, v2+1])
            v2 += 1
            # print(4, v1, v2, location)
            continue

        if location:
            v1, v2 = location[0][0], location[0][1]
            res += 1
    print(res)