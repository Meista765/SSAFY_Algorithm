# 벽 부수고 이동하기
import sys
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

'''
N*M 행렬
0: 길
1: 벽
(0, 0) --> (N-1, M-1) : 최단 경로 이동 (시작 칸, 도착 칸 포함)
벽 하나 부수고 이동하는 게 더 짧다면, 1개까진 부숴도 됨
상하좌우만 이동 가능
Q. 최단 거리를 구하라 (불가능하면 -1)
'''
# # DFS로 구현
# # 인자 : 현재 행, 현재 열, 이동한 거리, 벽 부쉈는지 여부
# def DFS(cur_r, cur_c, cnt, break_wall):
#     global min_cnt
#     # 현재까지 이동 거리가 최소 거리보다 크면 중지
#     if cnt > min_cnt:
#         return
    
#     # 도착하면 중지
#     if cur_r == N-1 and cur_c == M-1:
#         min_cnt = min(min_cnt, cnt)
#         return
    
#     # 아직 도착하기 전이면
#     else:
#         for k in range(4):
#             nr = cur_r + dr[k]
#             nc = cur_c + dc[k]
#             # 사방에 갈 곳 있으면
#             if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
#                 if arr[nr][nc]:     # 벽이면
#                     if not break_wall:      # 한번도 벽 부순적 없으면
#                         visited[nr][nc] = 1
#                         break_wall = True
#                         DFS(nr, nc, cnt+1, break_wall)
#                         visited[nr][nc] = 0
#                         break_wall = False
#                 else:   # 벽이 아니면
#                     visited[nr][nc] = 1
#                     DFS(nr, nc, cnt+1, break_wall)
#                     visited[nr][nc] = 0
        

# N, M = map(int, input().split())
# arr = [list(map(int, list(input().strip()))) for _ in range(N)]
# visited = [[0]*M for _ in range(N)]     # 방문 리스트
# dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]   # 우하좌상
# break_wall = False                      # 벽 부쉈는지 여부 초기값
# min_cnt = 1000000

# DEBUG = False

# if DEBUG:
#     print(N, M)
#     for i in range(N):
#         print(*arr[i])

# # 시작 위치가 벽이면 부수고 시작해
# if arr[0][0] == 1:
#     break_wall = True
# visited[0][0] = 1
# DFS(0, 0, 1, break_wall)

# if min_cnt == 1000000:
#     print(-1)
# else:
#     print(min_cnt)


# BFS로 구현 (더 효율적)
from collections import deque

def BFS():
    # 큐 생성 (행, 열, 이동 거리, 벽을 부쉈는지 여부)
    queue = deque([(0, 0, 1, 0)])
    visited[0][0][0] = 1  # [0]은 벽을 안 부쉈을 때, [1]은 벽을 부쉈을 때

    while queue:
        r, c, dist, wall_break = queue.popleft()
        
        # 도착 지점에 도달한 경우
        if r == N - 1 and c == M - 1:
            return dist
        
        # 상하좌우 이동
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            
            # 범위 내에 있고
            if 0 <= nr < N and 0 <= nc < M:
                # 벽이 아니고 방문한 적이 없다면
                if arr[nr][nc] == 0 and not visited[nr][nc][wall_break]:
                    visited[nr][nc][wall_break] = 1
                    queue.append((nr, nc, dist + 1, wall_break))
                
                # 벽이고, 아직 벽을 부순 적이 없다면
                elif arr[nr][nc] == 1 and wall_break == 0:
                    visited[nr][nc][1] = 1
                    queue.append((nr, nc, dist + 1, 1))
    
    # 도달할 수 없다면 -1 반환
    return -1

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
# 3차원 방문 배열
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]  # [0] 벽 안부숨, [1] 벽 부숨
dr = [0, 1, 0, -1]  # 우하좌상
dc = [1, 0, -1, 0]

print(BFS())