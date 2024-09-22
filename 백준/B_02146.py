import sys
sys.stdin = open('input.txt')
from collections import deque

# 섬 번호 매기기

def bfs_1(i,j,num):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1           # 방문표시
    arr[i][j] = num             # 섬 라벨링

    while q:
        v = q.popleft()
        for k in range(4):
            nr = v[0] + dr[k]
            nc = v[1] + dc[k]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] == 1:
                visited[nr][nc] = 1
                arr[nr][nc] = num
                q.append((nr,nc))

# 섬 연결하기
def bfs_2(n):
    q = deque()
    d = [[-1] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == n:
                d[i][j] = 0
                q.append((i,j))

    while q:
        v = q.popleft()
        for k in range(4):
            nr = v[0] + dr[k]
            nc = v[1] + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                # 다른 섬을 만났을 때
                if arr[nr][nc] != n and arr[nr][nc] != 0:
                    return d[v[0]][v[1]]
                # 물을 만났을 때 -> 다리 연결
                elif d[nr][nc] == -1 and arr[nr][nc] == 0:
                    d[nr][nc] = d[v[0]][v[1]] + 1
                    q.append((nr,nc))

    return 200



N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 섬 라벨링 작업
num = 1
for i in range(N):
    for j in range(N):
        if not visited[i][j] and arr[i][j] == 1:
            bfs_1(i,j,num)
            num += 1

# 최단거리구하기
min_val = 200
for n in range(1,num):
    result = bfs_2(n)
    min_val = min(result, min_val)

print(min_val)
