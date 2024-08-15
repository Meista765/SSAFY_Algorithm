import sys
sys.stdin = open('input.txt')
T = int(input())

for test_case in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 상하좌우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    max_sum = float('-inf')

    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            for k in range(4):
                for l in range(1,arr[i][j]+1):
                    nr = i + dr[k] * l
                    nc = j + dc[k] * l
                    if 0 <= nr < N and 0 <= nc < M:
                        cnt += arr[nr][nc]
            if max_sum < cnt:
                max_sum = cnt


    print(f'#{test_case} {max_sum}')



