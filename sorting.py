##########################Quick############################
def quick_sort(arr):
    a = arr[:]  # 원본 복사
    def _qsort(low, high):
        if low < high:
            pivot = a[high]
            i = low - 1
            for j in range(low, high):
                if a[j] <= pivot:
                    i += 1
                    a[i], a[j] = a[j], a[i]
            a[i+1], a[high] = a[high], a[i+1]
            pi = i + 1
            _qsort(low, pi - 1)
            _qsort(pi + 1, high)
    _qsort(0, len(a) - 1)
    return a
#########################Quick##############################
