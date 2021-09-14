def binarySearch(a, key, left, right):
    if left <= right:
        mid = int((left + right)/2)
        if key == a[mid]:
            print('key=%d, mid=%d'%(key, mid))
            return mid
        elif key < a[mid]:
            print('key=%d, mid=%d, [next] left=%d, right=%d'%(key, mid, left, mid-1))
            return binarySearch(a, key, left, mid-1)
        else:
            print('key=%d, mid=%d, [next] left=%d, right=%d'%(key, mid, mid+1, right))
            return binarySearch(a, key, mid+1, right)
    else:
        return -1


K = int(input('K = '))
A = list(range(100+1))
print(binarySearch(A, K, 1, 100))