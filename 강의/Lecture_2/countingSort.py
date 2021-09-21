def countingSort(a, n, m):
    count = [0] * (m+1)
    for i in range(1, n+1):
        count[a[i]] += 1
    for i in range(2, m+1):
        count[i] += count[i-1]
    b = [0] * (n+1)
    for i in range(n, 0, -1):
        b[count[a[i]]] = a[i]
        count[a[i]] -= 1
    for i in range(1, n+1):
        a[i] = b[i]

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if a[i] > a[i+1]:
            isSorted = False
        if not isSorted:
            break
    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")


import random, time

N = 100000
M = 1000
a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1, M))
start_time = time.time()
countingSort(a, N, M)
end_time = time.time() - start_time
print("계수 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))
checkSort(a, N)