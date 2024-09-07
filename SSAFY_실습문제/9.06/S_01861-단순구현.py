import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N * N + 1)
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]

                if 0 <= nr < N and 0 <= nc < N and arr[i][j] + 1 == arr[nr][nc]:
                    visited[arr[i][j]] = 1
                    break
    cnt = 0
    max_cnt = 0
    start = 0
    for i in range(N * N - 1, -1, -1):
        if visited[i] == 1:
            cnt += 1
        else:
            if max_cnt <= cnt:
                max_cnt = cnt
                start = i + 1
            cnt = 0
    print(f'#{test_case} {start} {max_cnt+1}')




