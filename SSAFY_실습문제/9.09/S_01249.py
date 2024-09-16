from collections import deque


def bfs(s):
    q = deque()
    q.append(s)
    d[s[0]][s[1]] = 0

    while q:
        v = q.popleft()
        for k in range(4):
            nr = v[0] + dr[k]
            nc = v[1] + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if d[nr][nc] > d[v[0]][v[1]] + arr[nr][nc]:
                    d[nr][nc] = d[v[0]][v[1]] + arr[nr][nc]
                    q.append((nr, nc))


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    d = [[float('inf')] * N for _ in range(N)]  # 최소 거리를 나타내는 2차원 배열
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    bfs((0, 0))
    print(f'#{test_case} {d[N - 1][N - 1]}')
