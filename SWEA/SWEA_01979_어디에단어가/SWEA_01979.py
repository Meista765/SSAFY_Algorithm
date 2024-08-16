import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_01979_어디에단어가/input.txt', 'r')

T = int(input())

# 행 하나 탐색
def row_search(arr, K):
    for c in range(N):
        if arr[c] == 1:
            one_cnt = 1
            for m in range(1, N):
                dc = c + m
                if (dc < N) and arr[dc] == 1:
                    one_cnt += 1
                else:
                    break
            if one_cnt == K:
                return 1
    return 0


# 열 하나 탐색
def col_search(matrix, K):
    pass

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    row_cnt = 0
    for row in puzzle:
        row_cnt += row_search(row, K)

    print(f'#{tc} {row_cnt}')

