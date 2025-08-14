##########################Quick############################
import sys
sys.setrecursionlimit(10**7)  # 재귀 깊이 제한 확장

def quick_sort(arr):
    a = arr[:]  # 원본 훼손 방지용 복사
    _quick_sort(a, 0, len(a) - 1)
    return a

def _partition(a, low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1

def _quick_sort(a, low, high):
    while low < high:
        pi = _partition(a, low, high)
        # Tail Recursion Optimization: 더 작은 구간 먼저 재귀
        if pi - low < high - pi:
            _quick_sort(a, low, pi - 1)
            low = pi + 1
        else:
            _quick_sort(a, pi + 1, high)
            high = pi - 1
###############################Quick#########################

