def find_index(idx):
    return real_list.index(idx)

def count(value):
    return real_list.count(value)

n, max_num = map(int, input().split(' '))
number_list = list(map(int, input().rstrip().split(' ')))
real_list = number_list.copy()
number_list.sort(key=lambda x: (-count(x), find_index(x)))
for x in number_list:
    print(x, end=' ')