import sys
sys.stdin = open('sample_input.txt', 'r', encoding='UTF-8')

def dfs2(i, j, N):
    visited[i][j] = 1   # 다녀왔다
    if maze[i][j] == 3: # 시작점이 3이면 1을 뱉어라
        return 1
    else:
        # 우 상 좌 하
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            # 이동할 좌표가 1이 아니고, 방문한 적이 없다면, 가라
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                # 이제 반복해라
                if dfs2(ni, nj, N):
                    return 1
        return 0

def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
    return -1, -1

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 출발 위치 찾기
    sti, stj = fstart(N)

    visited = [[0] * N for _ in range(N)] # dfs2 용
    print(f'#{tc} {dfs2(sti, stj, N)}')