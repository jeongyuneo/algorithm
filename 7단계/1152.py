a = input()
tmp_list = []
tmp = ''
for i in range(len(a)):
    if a[i].isalpha():
        tmp += a[i]
    elif a[i].isalpha() == False and tmp != '':
        tmp_list.append(tmp)
        tmp = ''
    if i == len(a) - 1 and a[i].isalpha():
        tmp_list.append(tmp)
print(len(tmp_list))