a = input().upper()
b = list(0 for i in range(27))
for i in a:
    b[ord(i) - 65] += 1

tmp_list = []
maxB = max(b)
for i in range(len(b)):
    if maxB == b[i]:
        tmp_list.append(i)

if len(tmp_list) == 1:
    print(chr(tmp_list[0] + 65))
else:
    print('?')