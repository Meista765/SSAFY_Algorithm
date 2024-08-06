import sys; sys.stdin = open('1208.txt')

def min_max(arr):
    min_idx = max_idx = 0
    for i in range(len(arr)):
        if arr[min_idx] > arr[i]:
            min_idx = i
        if arr[max_idx] < arr[i]:
            max_idx = i
    return min_idx, max_idx

for tc in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))

    # dump횟수만큼 반복
    for i in range(dump):
        # arr에서 최대/최소값의 인덱스 찾아서
        min_idx, max_idx = min_max(arr)

        arr[max_idx] -= 1
        arr[min_idx] += 1

    min_idx, max_idx = min_max(arr)

    print(f'#{tc} {arr[max_idx] - arr[min_idx]}')
