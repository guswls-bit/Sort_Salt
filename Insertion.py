import time

def insertion_sort(a: list[int]) -> list[int]:
    start = time.perf_counter()  # 시간 측정 시작

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

    elapsed = time.perf_counter() - start  # 시간 측정 종료
    print(f"[Insertion Sort] 소요 시간: {elapsed*1000:.2f} ms")
    print(f"[Insertion Sort] 결과 : {a}")