# 미로 탐색하기
import sys
#input = sys.stdin.readline
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

from collections import deque

def BFS(s_r, s_c):
    queue = deque()                 # 큐 만들기
    queue.appendleft((s_r, s_c))    # 출발 좌표 enqueue
    visited[s_r][s_c] = 1           # 출발 좌표 방문 표시
    
    while queue:    # 큐에 값이 없을 때까지 반복
        r, c = queue.pop()           # dequeue
        if r == N-1 and c == M-1:    # 만약 도착 지점에 도달했으면 
            return maze[r][c]        # 현 위치값 반환
        
        for i in range(4):      # 상, 하, 좌, 우 탐색
            # 주변이 벽이 아니면서 이미 갔던 곳이 아닌 경우 (갈 수 있는 곳인 경우)
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == 1 and not visited[nr][nc]:
                    queue.appendleft((nr, nc))      # 해당 좌표 enqueue
                    visited[nr][nc] = 1             # 해당 좌표 방문 표시
                    maze[nr][nc] += maze[r][c]      # 해당 위치값에 현재 위치값을 더하기

N, M = map(int, input().split())          # N*M 크기 미로
maze = [list(map(int, list(input().rstrip()))) for _ in range(N)]   # 미로
visited = [[0] * M for _ in range(N)]     # 방문 기록 저장 리스트

dr = [-1, 1, 0, 0]      # 델타 행
dc = [0, 0, -1, 1]      # 델타 열
print(BFS(0, 0))