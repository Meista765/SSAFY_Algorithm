import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())         # N: 행의 길이, M: 열 길이
    arr = [list(input()) for _ in range(N)]

    min_cnt = float('inf')

    # 배열 분할
    w_cnt = 0   # 하얀색으로 바꿔야 할 칸의 수
    for i in range(N-2):
        for w in range(M):
            if arr[i][w] != 'W':
                w_cnt += 1

        b_cnt = 0  # 파란색으로 바꿔야 할 칸의 수
        for j in range(i+1,N-1):
            for b in range(M):
                if arr[j][b] != 'B':
                    b_cnt += 1

            r_cnt = 0   # 빨간색으로 바꿔야 할 칸의 수
            for k in range(j+1,N):
                for r in range(M):
                    if arr[k][r] != 'R':
                        r_cnt += 1
            total_cnt = w_cnt + b_cnt + r_cnt
            if min_cnt > total_cnt:
                min_cnt = total_cnt

    print(f'#{test_case} {min_cnt}')




