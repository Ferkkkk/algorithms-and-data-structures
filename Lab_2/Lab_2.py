def max_heapify(A, n, i):
    l = left(i)
    r = right(i)
    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def build_max_heap(A):
    n = len(A)
    for i in range(n, -1, -1):
        max_heapify(A, n, i)
    print(A)


def heap_sort(A):
    build_max_heap(A)
    n = len(A)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A, i, 0)


A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heap_sort(A)
print(A)