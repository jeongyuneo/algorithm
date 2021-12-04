import sys

n = int(input())
number_list = list(int(sys.stdin.readline()) for _ in range(n))
number_list.sort()
for value in number_list:
    print(value)