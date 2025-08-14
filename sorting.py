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
#########################Quick##############################

if __name__ == "__main__":
    data = load_data()
    quick_sort(data)  # 여기서 이미 결과와 시간 출력

