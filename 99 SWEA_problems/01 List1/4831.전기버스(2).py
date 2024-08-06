import sys; sys.stdin = open('4831.txt')
T = int(input())
for tc in range(1, T + 1):
    K, N, M = tuple(map(int, input().split()))
    # [0] + [1, 3, 5, 7, 9] + [N]
    arr = [0] + list(map(int, input().split())) + [N]

    cur = ans = 0
    for i in range(1, M + 2):
        # 1. 안되는 경우 인접한 두 청전소의 거리가 K보다 크면
        if arr[i - 1] + K < arr[i]:
            ans = 0
            break
        # 2. arr[i] 충전소가 cur + K 범위를 벗어나면 그 이전 충전소에서 충전
        if cur + K < arr[i]:
            cur = arr[i - 1]
            ans += 1

    print(f'#{tc} {ans}')







