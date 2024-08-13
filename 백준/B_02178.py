from collections import deque

N, M = map(int,input().split())
maze = [[0] * M for _ in range(N)]           # 미로
visited = [[0]*M for _ in range(N)]         # 방문리스트

for i in range(N):
    numbers = list(input())
    for j in range(M):
        maze[i][j] = int(numbers[j])

start = (0,0)
end = (N-1,M-1)

def BFS(s):
    dr = [-1, 1, 0, 0]  # 상하좌우
    dc = [0, 0, -1, 1]
    q = deque()
    q.append(s)
    visited[s[0]][s[1]] = 1     # 방문리스트 체크
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == 1 and visited[nr][nc] == 0:
                q.append((nr,nc))
                visited[nr][nc] = 1
                maze[nr][nc] = maze[r][c] + 1
BFS(start)
print(maze[N-1][M-1])