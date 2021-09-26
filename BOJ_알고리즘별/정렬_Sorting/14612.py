import sys

N, M = map(int, sys.stdin.readline().rsplit(' '))
order_list = []
for i in range(N):
    data = list(sys.stdin.readline().rstrip().split(' '))
    if data[0] == 'order':
        order_list.append([int(data[1]), int(data[2])])
    elif data[0] == 'sort':
        order_list.sort(key=lambda x:(x[1], x[0]))
    else:
        for k in order_list:
            if k[0] == int(data[1]):
                order_list.remove(k)
    if order_list:
        for j in order_list:
            print(j[0], end=' ')
        print()
    else:
        print('sleep')