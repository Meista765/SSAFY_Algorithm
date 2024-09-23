import sys
sys.stdin = open('input.txt')
from collections import deque
from heapq import heappop,heappush


# 섬 라벨링
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(i,j,label):
    q = deque([(i,j)])
    visited[i][j] = 1
    arr[i][j] = label
    while q:
        v = q.popleft()
        for k in range(4):
            nr = v[0] + dr[k]
            nc = v[1] + dc[k]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc] == 1:
                arr[nr][nc] = label
                visited[nr][nc] = 1
                q.append((nr,nc))

# 섬 연결하기
def bfs_2(n,G):
    q = deque()
    d = [[-1] * M for _ in range(M)]


    while q:




N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]       # 방문 정보

# 섬 라벨링 작업
label = 1
for i in range(N):
    for j in range(M):
        if not visited[i][j] and arr[i][j] == 1:
            bfs(i,j,label)
            label += 1

G = [[] for _ in range(label+1)]
