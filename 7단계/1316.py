n = int(input())
cnt = 0
for i in range(n):
    a = input()
    tmp_str = list(a[0])
    tmp = a[0]
    is_group_word = True

    for j in range(1, len(a)):
        if a[j] != tmp and a[j] not in tmp_str:
            tmp_str.append(a[j])
            tmp = a[j]
        elif a[j] != tmp and a[j] in tmp_str:
            is_group_word = False
            break
    if is_group_word:
        cnt += 1
print(cnt)