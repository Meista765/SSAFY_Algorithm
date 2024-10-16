# 안전 영역
import sys
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

from collections import deque

def BFS(start_r, start_c, rain):
    global visited
    
    queue = deque()
    queue.append([start_r, start_c])
    visited[start_r][start_c] = 1
    
    while queue:
        r, c = queue.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] > rain:
                queue.append([nr, nc])
                visited[nr][nc] = 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

max_height = max(map(max, arr))         # 지역 전체에서 가장 높은 지점 구하기
max_cnt = 0

for rain in range(max_height):          # 비 내리는 양
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and arr[r][c] > rain:
                BFS(r, c, rain)
                cnt += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)