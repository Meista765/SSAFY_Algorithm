import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_01979_어디에단어가/input.txt', 'r')

T = int(input())

# 배열 하나 탐색
def K_search(arr, K):        
    N = len(arr)
    one_cnt = 0
    for c in range(N):
        if arr[c] == 1:
            one_cnt += 1
        else:
            if one_cnt == K:
                return 1
            else:
                one_cnt = 0
    if one_cnt == K:
        return 1
    else:
        return 0

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    row_cnt = 0
    for row in puzzle:
        row_cnt += K_search(row, K)

        # 열 다시 생각해보기
#     for j in range(N):
#         col_cnt = 0
#         col_arr = []
#         for i in range(N):
#             col_arr.append(puzzle[i][j])
#         col_cnt += K_search(col_arr, K)
    
#     ans = row_cnt + col_cnt
    
    print(f'#{tc} {row_cnt}')

