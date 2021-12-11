def count_value(li, key):
    count = 0
    for value in li:
        if value[1][:3] == key:
            count += 1
    return count

n, k = map(int, input().split())
nations = {}
for i in range(n):
    nation, gold, silver, bronze = map(int, input().split())
    nations[nation] = [gold, silver, bronze]
res = sorted(nations.items(), key=lambda x: (x[1][0], x[1][1], x[1][2]), reverse=True)
i, ranking = 0, 1
while i < n:
    count = count_value(res, res[i][1])
    if count == 1:
        res[i][1].append(ranking)
        ranking += 1
    else:
        for j in range(count):
            res[i+j][1].append(ranking)
        i += count-1
        ranking += count
    i += 1
res_dict = {}
for i in range(n):
    res_dict[res[i][0]] = res[i][1]
print(res_dict[k][3])