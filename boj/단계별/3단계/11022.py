a = int(input())
for i in range(a):
    n, m = map(int, input().split())
    print('Case #%d: %d + %d = %d'%(i+1, n, m, n+m))