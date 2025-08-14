import time

def bubble_sort(arr):
    """
    버블 정렬 알고리즘
    """
    n = len(arr)
    
    for i in range(n - 1):
        swapped = False
        
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # 두 원소 교환
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 교환이 일어나지 않았으면 정렬 완료
        if not swapped:
            break
    
    return arr

# 데이터 읽기
with open('data.txt', 'r') as file:
    data = [int(x.strip()) for x in file.read().split(',')]

print("=== 버블 정렬 ===")
print("정렬 전:", data)

# 정렬 시간 측정
start_time = time.time()
sorted_data = bubble_sort(data.copy())  # 원본 보존을 위해 복사
end_time = time.time()

# 결과 출력
print("정렬 후:", sorted_data)
print(f"정렬 시간: {end_time - start_time:.6f}초")
print(f"데이터 개수: {len(data)}개")