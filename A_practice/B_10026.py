# 적록색약
import sys
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

'''
적록색약은 빨/초 차이 느끼지 못함
'''
from collections import deque
              
def BFS(start_r, start_c, color):
    # 큐 생성
    queue = deque()
    
    # 시작 좌표 enqueue하고 방문 표시
    queue.append([start_r, start_c])
    visited[start_r][start_c] = 1

    while queue:
        r, c = queue.popleft()
        # 상하좌우 탐색
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            # 배열을 벗어나지 않고, 방문한적 없으며, 시작점과 같은 색깔이면 큐에 넣고 방문 표시
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] in color:
                queue.append([nr, nc])    
                visited[nr][nc] = 1
    return

#===============================================================
N = int(input())                                    # 그림 크기
arr = [list(input().strip()) for _ in range(N)]     # 그림

# 델타
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0] 

# 정상인
cnt = 0                                   # 본 구역의 개수
visited = [[0]*N for _ in range(N)]       # 방문 리스트 초기화
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            BFS(r, c, arr[r][c])
            cnt += 1
print(cnt, end=' ')
    
# 색맹
cnt = 0                                   # 본 구역의 개수
visited = [[0]*N for _ in range(N)]       # 방문 리스트 초기화
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            if arr[r][c] == 'B':
                color = 'B'
            else:
                color = 'RG'
            BFS(r, c, color)
            cnt += 1    
print(cnt)