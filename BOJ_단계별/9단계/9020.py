def partition(a, b):
    index = 0
    while True:
        half_num = int(b/2)
        if a[half_num-index] and a[half_num+index]:
            return half_num-index, half_num+index
        index += 1

def eratos(a):
    l = [1] * (a+1)
    l[0], l[1] = 0, 0
    for i in range(2, int(math.sqrt(a))+1):
        if l[i]:
            j = 2
            while i*j <= a:
                l[i*j] = 0
                j += 1
    return l

import math
n = int(input())
for i in range(n):
    m = int(input())
    primes = eratos(m)
    result = partition(primes, m)
    print(result[0], result[1])