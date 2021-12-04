import sys

n = int(input())
number_list = list(int(sys.stdin.readline()) for _ in range(n))
number_list.sort(reverse=True)
for value in number_list:
    print(value)