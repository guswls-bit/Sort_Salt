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
