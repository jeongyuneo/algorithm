def heapSort(a, n):
    for i in range(n, 1, -1):
        heapify(a, i)
        # print('히프화', a, '히프크기', n)
        a[1], a[i] = a[i], a[1]
        # print('교환', a, i-1)
        # heapSort(a, n-1)

def heapify(a, n):
    # 히프 구조로 변환
    b = list(a)
    b.sort()
    for i in range(n, 0, -1):
        j = a.index(b[i])
        while j//2 > 0:
            if a[j//2] < a[j]:
                a[j//2], a[j] = a[j], a[j//2]
            j //= 2

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
a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1, N))
# a = [-1, 6, 2, 8, 1, 3, 9, 4, 5, 10, 7]
# N = 10
start_time = time.time()
heapSort(a, N)
end_time = time.time() - start_time
print("힙 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))
checkSort(a, N)