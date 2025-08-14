def insertion_sort(a: List[int]) -> List[int]:
    import time
    start = time.time()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    end = time.time()
    print(f"삽입 정렬 결과: \n{a}")
    print(f"소요 시간: {end - start:.6f}초")
