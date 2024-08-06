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
    return merge(left_,right_)s

def merge(left, right):
    left_idx = 0
    right_idx = 0 # 투포인터 활용
    result =[]

    while left_idx < len(left) and right_idx < len(right):   
        if left[left_idx] > right[right_idx]:           ## 왼쪽데이터의 left_idx가 가리키는 값이 오른쪽 데이터의 right_idx가 가리키는 값보다 크면
            result.append(right[right_idx])             ## 오른쪽 데이터의 right_idx가 가리키는 값을 result에 입력하고 right_idx를 오른쪽으로 한칸 이동
            right_idx += 1
        else:
            result.append(left[left_idx])               ## 오른쪽 데이터의 right_idx가 가리키는 값이 오른쪽 데이터의 left_idx가 가리키는 값보다 크면
            left_idx += 1                               ## 왼쪽 데이터의 left_idx가 가리키는 값 result에 입력하고 left_idx를 오른쪽으로 한칸 이동
    
    while left_idx < len(left):                         ## 위의 while문이 끝나고 남은 데이터들 입력
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

