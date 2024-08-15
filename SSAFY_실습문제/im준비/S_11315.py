import sys
sys.stdin = open('input.txt')
T = int(input())

def check(N,arr):
    # 우, 하, 우상~좌하 대각선, 좌상~우하 대각선
    dr = [0, 1, 1, 1]
    dc = [1, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':

                # 4가지 방향에 대해서 탐색
                for k in range(4):
                    cnt = 1
                    nr = i + dr[k]
                    nc = j + dc[k]

                    while 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'o':
                        cnt += 1
                        nr += dr[k]
                        nc += dc[k]
                        if cnt == 5:
                            return 'YES'
    return 'NO'


for test_case in range(1,T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    result = check(N,arr)
    print(f'#{test_case} {result}')
