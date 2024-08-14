from collections import deque
import sys
sys.stdin = open('input.txt')
def find_start():               # 출발노드 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return (i,j)


def bfs(s):
    q = deque()
    q.append(s)
    visited[s[0]][s[1]] = 1
    # 상하좌우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    while q:
        v = q.popleft()
        # 도착지점인지 확인
        if maze[v[0]][v[1]] == 3:
            return visited[v[0]][v[1]] -1 -1

        for k in range(4):
            nr = v[0] + dr[k]
            nc = v[1] + dc[k]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and maze[nr][nc] != 1:
                q.append((nr,nc))
                visited[nr][nc] = visited[v[0]][v[1]] + 1
    return 0

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    start = find_start()
    result = bfs(start)

    print(f'#{test_case} {result}')

