import sys
#input = sys.stdin.readline

N, K = map(int, input().split())             # N: 숫자 개수, K: 출력하고 싶은 수 위치 (K번째)
arr = list(map(int, input().split()))        # 배열

pivot = K-1     # 피벗 위치
start = 0       # 시작 지점
end = N-1       # 끝 지점

def quick_sort(pivot, start, end):
    global arr
    if start + 1 == end:            # 원소가 2개밖에 없으면
        if arr[start] > arr[end]:                           # 왼쪽이 오른쪽보다 클 경우
            arr[start], arr[end] = arr[end], arr[start]     # 서로 자리 변경
            pivot = end 
