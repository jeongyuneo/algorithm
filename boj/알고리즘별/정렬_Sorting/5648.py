string_list = list(map(str, input().split()))
n = int(string_list.pop(0))
while len(string_list) != n:
    string_list.extend(list(map(str, input().split())))
result = []
for value in string_list:
    number = 0
    for i in range(len(value)-1, -1, -1):
        number *= 10
        number += int(value[i])
    result.append(number)
for value in sorted(result):
    print(value)