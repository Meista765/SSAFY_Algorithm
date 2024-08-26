import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    max_val = 0

    # 하 우 만 살펴보면 된다.
    dr = [1,0]
    dc = [0,1]
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                for k in range(2):
                    cnt = 1
                    nr = r + dr[k]
                    nc = c + dc[k]
                    while nr < N and nc < M and arr[nr][nc] == 1:
                        cnt += 1
                        nr += dr[k]
                        nc += dc[k]

                    if cnt > max_val:
                        max_val = cnt
    if max_val == 1:
        max_val = 0
    
    print(f'#{test_case} {max_val}')


