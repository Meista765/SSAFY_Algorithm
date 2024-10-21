import sys
sys.stdin = open('sample_input.txt', 'r')

di = [-1, -1, 1, 1]
dj = [1, -1, -1, 1]


def des(i, j, d): # i,j는 시작하는 좌표의 행,열 d는 방향이다.
    global max_V
    if d < 3:
        tmp = d + 2
    else:
        tmp = d + 1
    for k in range(d, tmp): # 현재 오는 방향, 그 다음방향으로 2가지 선택지가 있다
        ni, nj = i + di[k], j + dj[k]
        if si == ni and sj == nj: # 처음 시작점으로 돌아오는 경우, max값 갱신
            max_V = max(sum(dessert), max_V)
            return
        if 0 <= ni < N and 0 <= nj < N :
            if not dessert[arr[ni][nj]]: # 이전에 먹은 디저트가 아니라면,
                dessert[arr[ni][nj]] = 1
                des(ni, nj, k)
                dessert[arr[ni][nj]] = 0
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    max_V = -1
 
    # 탐색을 시작 할 좌표 선택
    for i in range(N - 2):
        for j in range(1, N - 1):
            si, sj = i, j
            dessert = [0]*101
            dessert[arr[si][sj]] = 1
            des(si, sj, 0)
 
    print(f"#{tc} {max_V}")


