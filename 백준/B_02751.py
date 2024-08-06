import sys
input = sys.stdin.readline
print = sys.stdout.write

# 분할 및 병합 정렬

def merge_sort(arr):
    # 크기가 1일 때 까지
    if len(arr) <= 1:
        return arr
    
    # 리스트 2분할
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # 게속 쪼개자 1일 될때까지
    left_ = merge_sort(left)
    right_ = merge_sort(right)
    return merge(left_,right_)

def merge(left, right):
    left_idx = 0
    right_idx = 0 # 투포인터 활용
    result =[]

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] > right[right_idx]:
            result.append(right[right_idx])
            right_idx += 1
        else:
            result.append(left[left_idx])
            left_idx += 1
    while left_idx < len(left):
        result.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        result.append(right[right_idx])
        right_idx += 1

    return result

N = int(input())

arr = [int(input()) for _ in range(N)]

result = merge_sort(arr)

for i in range(N):
    print(str(result[i])+ '\n')

