
T = int(input())

def rect_sum(arr, N, r1, c1, M):
    total = 0
    for r in range(r1, r1 + M):
        for c in range(c1, c1 + M):
            total += arr[r][c]
    return total

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    # 모든 사각 영역의 시작점
    for r in range(N-M + 1):
        for c in range(N-M + 1):
            ret = rect_sum(arr, N, r, c, M)
            if ans < ret:
                ans = ret
    print(f'{tc} {ans}')