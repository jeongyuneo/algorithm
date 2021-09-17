def mergeSort(a, l, r):
    if r > l:
        m = (r+l)//2
        mergeSort(a, l, m)
        mergeSort(a, m+1, r)
        merge(a, l, m, r)

def merge(a, l, m, r):
    tmp = []
    i, j = l, m+1
    while i <= m and j <= r:
        if a[i] < a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    if i <= m:
        tmp.extend(a[i:m+1])
    else:
        tmp.extend(a[j:r+1])
    a[l:r+1] = tmp


def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if a[i] > a[i + 1]:
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
a.append(None)
for i in range(N):
    a.append(random.randint(1, N))
# a = [-1, 6, 2, 8, 1, 3, 9, 4, 5, 10, 7]
# N = 10
start_time = time.time()
mergeSort(a, 1, N)
end_time = time.time() - start_time
print("합병 정렬의 실행 시간 (N=%d) : %0.3f" % (N, end_time))
checkSort(a, N)

"""
# 모범답안
def mergeSort(a, l, r):
    if r > l:
        b = a
        m = (r+l)//2
        mergeSort(a, l, m)
        mergeSort(a, m+1, r)
        i, j, k = l, m+1, l
        while i <= m and j <= r:
            if a[i] < a[j]:
                b[k] = a[i]
                k += 1
                i += 1
            else:
                b[k] = a[j]
                k += 1
                j += 1
        if i > m:
            for p in range(j, r+1):
                b[k] = a[p]
                k += 1
        else:
            for p in range(i, m+1):
                b[k] = a[p]
                k += 1
        for p in range(l, r+1):
            a[p] = b[p]

"""