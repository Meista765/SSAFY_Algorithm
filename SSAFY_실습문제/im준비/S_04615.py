import sys
sys.stdin = open('input.txt')
T = int(input())

for test_case in range(1,T+1):
    N, M = map(int,input().split())         # N: 보드의 길이, M: 돌을 놓는 횟수
    arr = [[0] * N for _ in range(N)]       # 바둑판

    # 바둑판 초기 세팅
    arr[N//2-1][N//2-1] = 2
    arr[N//2-1][N//2] = 1
    arr[N//2][N//2-1] = 1
    arr[N//2][N//2] = 2

    # 상,하,좌,우,우상향,좌상향,우하향,좌하향
    dx = [1, 1, 0, -1, -1, -1,  0,  1]  # 좌우
    dy = [0, 1, 1,  1,  0, -1, -1, -1]  # 위아래

    colors = [0, 2, 1]

    for l in range(M):
        x,y,color = map(int,input().split())    # x: col, y = row, color: 흑(1) or 백(2)
        arr[y-1][x-1] = color

        for k in range(8):
            temp = []
            ny = y-1 + dy[k]
            nx = x-1 + dx[k]
            if color == 1:                 # 흑돌이면
                while 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 2: # 인덱스를 벗어나거나
                    temp.append((ny,nx))                                # 해당 칸이 비었거나 흑돌을 만나면 멈춤
                    ny += dy[k]
                    nx += dx[k]
                if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 1:    # 인덱스를 벗어나지 않고
                    for r,c in temp:                                    # 흑돌이여서 멈췄을 경우
                        arr[r][c] = 1

            if color == 2:  # 백돌이면
                while 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 1:  # 인덱스를 벗어나거나
                    temp.append((ny, nx))                                # 해당 칸이 비었거나 백돌을 만나면 멈춤
                    ny += dy[k]
                    nx += dx[k]
                if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 2:     # 인덱스를 벗어나지 않고
                    for r, c in temp:                                    # 백돌이여서 멈췄을 경우
                        arr[r][c] = 2

    b_cnt = 0
    w_cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                b_cnt += 1
            elif arr[i][j] == 2:
                w_cnt += 1


    print(f'#{test_case} {b_cnt} {w_cnt}')



