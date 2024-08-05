import sys
#input = sys.stdin.readline

N, K = map(int, input().split())        # N: 숫자 개수, K: 출력하고 싶은 수 위치 (K번째)
arr = list(map(int, input().split()))   # 배열


def quick_sort(start, end, K):
    global arr
    
    if start < end:
        pivot = partitions(start, end)
        if pivot == K:      # K번째 수가 pivot이면 더는 구할 필요 없음
            return
        elif K < pivot:     # K가 pivot보다 작으면 왼쪽 그룹만 정렬
            quick_sort(start, pivot - 1, K)
        else:               # K가 pivot보다 크면 오른쪽 그룹만 정렬
            quick_sort(pivot+1, end, K)


def partitions(start, end):
    global arr
    
    # 원소가 두 개밖에 없고, 순서가 반대면 두 개 스왑
    if start + 1 == end:
        if arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
    
    # 중간값과 가장 첫 값 위치를 바꾸기
    mid = (start + end) // 2
    arr[mid], arr[start] = arr[start], arr[mid]
    
    # 피벗 위치를 start 위치로, i와 j를 시작점 끝점으로 설정
    pivot = arr[start]
    i = start + 1
    j = end
    
    # i, j가 같아질 때까지 pivot 값 기준으로 스왑
    while i <= j:
        while arr[i] < pivot and i < len(arr)-1:
            i += 1
        while arr[j] > pivot and j > 0:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    
    # 피벗의 값을 양쪽으로 분리한 가운데에 오도록 설정
    arr[start] = arr[j]  # 원래 피벗 있던 가장 첫번째 자리는 i==j 위치 값 넣고
    arr[j] = pivot       # i==j 위치에는 기존 피벗 값을 집어넣기
    
    return j   # i==j 위치에 피벗이 들어갔으므로, 현재 피벗 위치를 반환한 것


quick_sort(0, N-1, K-1)
print(arr[K-1])


    
