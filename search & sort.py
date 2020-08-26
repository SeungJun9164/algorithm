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

