def radixSort(a, n, m, q):
    for i in range(1, m+1):
        for j in range(1, n+1):
            kd = digit(a[j], i)
            enqueue(q[kd], a[j])
        p = 0
        for j in range(10):
            while q[j]:
                p += 1
                a[p] = dequeue(q[j])

def digit(d, k):
    tmp = 1
    for i in range(1, k):
        tmp *= 10
    d //= tmp
    d %= 10
    return d

def enqueue(queue, data):
    queue.append(data)

def dequeue(queue):
    if not queue:
        return -1
    return queue.pop(0)

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
M = 5
a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1, 99999))
Q = []
for i in range(10):
    Q.append([])
start_time = time.time()
radixSort(a, N, M, Q)
end_time = time.time() - start_time
print("기수 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))
checkSort(a, N)