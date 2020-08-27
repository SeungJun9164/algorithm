# 순차 탐색
arr = [17, 9, 2, 18, 33, 58, 5, 34, 42]
def search_list(a, x):
    n = len(a)
    for i in range(n):
        if a[i] == x:
            return i+1
    return -1
print(search_list(arr, 58))

# 선택 정렬
def find_sort_list(a):
    n = len(a)
    for i in range(0, n - 1):
        idx = i
        for j in range(i + 1, n):
            if a[j] < a[idx]:
                idx = j
        a[i], a[idx] = a[idx], a[i]
find_sort_list(arr)
print(arr)

# 삽입 정렬
def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
d = [2, 4, 5, 1, 3]
ins_sort(d)
print(d)

# 병합 정렬
def merge(left, right):
    arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    if i <= len(left):
        arr = arr + right[j:]
    if j <= len(right):
        arr = arr + left[i:]
    return arr

def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    mid = n // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(d))

# 퀵 정렬
def quick_sort_sub(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a) - 1]
    left, right, equal = [], [], []
    for i in a:
        if i < pivot:
            left.append(i)
        elif i == pivot:
            equal.append(i)
        elif i > pivot:
            right.append(i)
    return quick_sort_sub(left) + equal + quick_sort_sub(right)

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort_sub(d))

# 버블 정렬
def BubbleSort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(BubbleSort(d))
