import sys
#input = sys.stdin.readline
N = int(input())   # 수의 개수
arr = [int(input()) for _ in range(N)]   # 배열


def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:  # 더 이상 나눌 수 없으면 끝내기
            return
        # 반으로 나눠서 두 그룹을 각각 재귀적으로 정렬
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        # 정렬된 두 부분 배열 병합 -> 하나의 정렬된 배열
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []  
        l, h = low, mid
        
        # 첫 번째 부분 배열, 두 번째 부분 배열의 요소들을 비교
        while l < mid and h < high:
            # 양쪽 그룹으로 나눠서 
            if arr[l] < arr[h]:      # 왼쪽이 더 작으면 먼저 temp에 넣기
                temp.append(arr[l])
                l += 1
            else:                    # 오른쪽이 더 작으면 먼저 temp에 넣기
                temp.append(arr[h])
                h += 1

        # 첫 번째 부분 배열에 남은 요소가 있으면 모두 temp에 추가
        while l < mid:
            temp.append(arr[l])
            l += 1
        # 두 번째 부분 배열에 남은 요소가 있으면 모두 temp에 추가
        while h < high:
            temp.append(arr[h])
            h += 1

        # temp에 저장된 병합된 결과를 원본 배열 arr의 해당 위치에 복사
        for i in range(low, high):
            arr[i] = temp[i - low]   # 만약 low가 3이라면 3-3해줘야 0이 됨

    return sort(0, len(arr))   # 정렬 시작하기 위해 sort함수 처음 호출


merge_sort(arr)
for num in arr:
    print(num)