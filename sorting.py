import re
from time import perf_counter

def load_data(path="data.txt"):
    with open(path, "r", encoding="utf-8") as f:
        s = f.read()
    parts = re.split(r"[\s,]+", s.strip())
    return [int(p) for p in parts if p != ""]

##########################Quick#############################
def quick_sort(data):
    import time
    a = data[:]  # 원본 복사
    start = time.perf_counter()

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
    elapsed = time.perf_counter() - start
    print("퀵정렬 결과:")
    print(a)
    print(f"소요 시간: {elapsed:.6f}초")

#########################Bubble#############################
def bubble_sort(data):
    import time
    a = data[:]  # 원본 복사
    start = time.perf_counter()
    n = len(a)
    
    for i in range(n - 1):
        swapped = False
        
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                # 두 원소 교환
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        
        # 교환이 일어나지 않았으면 정렬 완료
        if not swapped:
            break
    
    elapsed = time.perf_counter() - start
    print("버블 정렬 결과:")
    print(a)
    print(f"소요 시간: {elapsed:.6f}초")
#########################Select#############################
def select(input_list):
    import time
    start = time.time()
    for i in range(len(input_list)):
        for j in range(len(input_list)-(i+1)):
            if input_list[i] > input_list[i+j+1]:
                temp = input_list[i]
                input_list[i] = input_list[i+j+1]
                input_list[i+j+1] = temp
            else:
                continue
    end = time.time()
    print(f"선택 정렬 결과: \n{input_list}")
    print(f"소요 시간: {end - start:.6f}초")

#########################Merge#############################
def merge_sort_with_time(arr):
    import time
    def merge_sort(lst):
        if len(lst) <= 1:
            return lst

        mid = len(lst) // 2
        left_half = merge_sort(lst[:mid])
        right_half = merge_sort(lst[mid:])

        return merge(left_half, right_half)

    def merge(left, right):
        sorted_list = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])

        return sorted_list

    # 시간 측정 시작
    start_time = time.perf_counter()
    sorted_data = merge_sort(arr)
    end_time = time.perf_counter()

    # 결과 출력
    print(f"병합 정렬 결과:\n{sorted_data}")
    print(f"소요 시간: {end_time - start_time:.6f}초")
#########################Main##############################
if __name__ == "__main__":
    data = load_data()
    quick_sort(data)  # 여기서 이미 결과와 시간 출력
    print()  # 줄 바꿈
    bubble_sort(data)  # 버블 정렬도 실행
    print()
    select(data)
    print()
    merge_sort_with_time(data)
