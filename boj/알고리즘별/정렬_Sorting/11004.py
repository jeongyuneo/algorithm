n, k = map(int, input().split())
number_list = list(map(int, input().split()))
print(sorted(number_list)[k-1])