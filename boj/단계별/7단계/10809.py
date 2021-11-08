a = input()
b = list(chr(i) for i in range(97, 123))
c = list('' for i in range(len(b)))
for i in range(len(b)):
    for j in range(len(a)):
        if a[j] == b[i] and c[i] == '':
            c[i] = j
for i in range(len(c)):
    if c[i] != '':
        print(c[i], end=' ')
    else:
        print('-1', end=' ')