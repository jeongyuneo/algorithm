def sumNumbers(s):
    result = 0
    for x in s:
        if x.isnumeric():
            result += int(x)
    return result

import sys

n = int(input())
serial_list = list(sys.stdin.readline().rstrip() for _ in range(n))
serial_list.sort(key=lambda x: (len(x), sumNumbers(x), x))
for value in serial_list:
    print(value)
