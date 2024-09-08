import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = 1

    while q:
        v = q.popleft()
        for dr, dc in types[arr[v[0]][v[1]]]:
            nr = v[0] + dr
            nc = v[1] + dc
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] != 0:     # 인덱스를 벗어나지 않고 방문하지 않았다면
                if (-dr, -dc) in types[arr[nr][nc]]:   # 연결이 가능하다면
                    visited[nr][nc] = visited[v[0]][v[1]] + 1
                    q.append((nr, nc))


T = int(input())
for test_case in range(1,T+1):
    N, M, R, C, L = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    # 터널 상태에 따른 방향 확인
    types = {
        0: (),
        1: ((-1, 0), (1, 0), (0, -1), (0, 1)),  # 상하좌우
        2: ((-1, 0), (1, 0)),                   # 상하
        3: ((0, -1), (0, 1)),                   # 좌우
        4: ((-1, 0), (0, 1)),                   # 상우
        5: ((1, 0), (0, 1)),                    # 하우
        6: ((1, 0), (0, -1)),                   # 하좌
        7: ((-1, 0), (0, -1))                   # 상
    }
    bfs(R,C)
    # for k in range(N):
    #     print(*visited[k])
    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1
    print(f'#{test_case} {cnt}')