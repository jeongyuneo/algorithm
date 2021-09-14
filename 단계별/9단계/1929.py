def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

import math
a, b = map(int, input().split())
for j in range(a, b+1):
    if isPrime(j):
        print(j)
