def eratos(n):
    c = [1]*(n+1)
    c[0], c[1] = 0, 0
    for i in range(2, int(math.sqrt(n)) + 1):
        j = 2
        if c[i]:
            while i*j <= n:
                c[i*j] = 0
                j += 1
    return c

import math
n = int(input())
while n != 0:
    res = eratos(n*2)
    print(sum(res[n+1:n*2+1]))
    n = int(input())