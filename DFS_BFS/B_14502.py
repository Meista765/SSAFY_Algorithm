import sys
from collections import deque
from copy import deepcopy
from itertools import combinations 
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#input = sys.stdin.readline

def BFS(tmp_arr):
    global spread_min
    queue = deque(virus_pos_lst)
    spread_cnt = 0              # 바이러스 퍼진 칸 개수
    
    while queue:
        r, c = queue.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            # 지도를 벗어나지 않고, 빈 칸이면 바이러스 퍼뜨리기
            if 0 <= nr < N and 0 <= nc < M and tmp_arr[nr][nc] == 0:
                tmp_arr[nr][nc] = 2     # 바이러스 퍼진 칸 2로 바꾸고
                spread_cnt += 1         # 개수 1개 증가시키고
                queue.append((nr, nc))  # 거기서 더 퍼질 수 있게 큐에 넣어주기

    spread_min = min(spread_min, spread_cnt)


N, M = map(int, input().split())    # N: 세로 크기, M: 가로 크기
arr = [list(map(int, input().split())) for _ in range(N)]   # 지도
spread_min = N*M                    # 바이러스 퍼진 칸 최소 개수
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# 바이러스 위치 찾기 & 0 개수 세기
virus_pos_lst = []      # 바이러스들 위치 넣을 리스트
zero_pos_lst = []       # 바이러스 퍼지기 전 안전 영역 위치 리스트        
for r in range(N):
    for c in range(M):
        if arr[r][c] == 2:
            virus_pos_lst.append((r, c))
        if arr[r][c] == 0:
            zero_pos_lst.append((r, c))

# 3개의 벽을 세울 수 있는 모든 경우 구하고 각각에 대해 BFS
for three_walls in combinations(zero_pos_lst, 3):
    tmp_arr = deepcopy(arr)     # 원래 배열을 딥카피해서 사용(벽 세우고 바이러스도 퍼질 거라서)
    for wall_pos in three_walls:
        row, col = wall_pos
        tmp_arr[row][col] = 1
    BFS(tmp_arr)


# (바이러스 퍼지기 전 0 개수) - (바이러스 최소로 퍼졌을 때의 퍼진 칸 개수) - (새로 세워진 벽 3개) 
print(len(zero_pos_lst) - spread_min - 3)



#======================================================================================
def BFS():
    global spread_min
    queue = deque(virus_pos_lst)
    tmp_arr = deepcopy(arr)  # 바이러스 퍼지기 위한 딥카피
    spread_cnt = 0           # 퍼진 바이러스 칸 수
    
    while queue:
        r, c = queue.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and tmp_arr[nr][nc] == 0:
                tmp_arr[nr][nc] = 2  # 바이러스가 퍼짐
                spread_cnt += 1
                queue.append((nr, nc))

    spread_min = min(spread_min, spread_cnt)

def backtrack(start, cnt):
    # 벽 3개를 세웠으면 BFS 실행
    if cnt == 3:
        BFS()
        return

    for i in range(start, N * M):
        y, x = divmod(i, M)
        if arr[y][x] == 0:  # 빈 칸에만 벽 세우기
            arr[y][x] = 1    # 벽 세우기
            backtrack(i + 1, cnt + 1)  # 다음 위치로 이동
            arr[y][x] = 0    # 벽 허물기 (백트래킹)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
spread_min = N * M
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# 바이러스 위치 찾기 및 빈 칸 수 세기
virus_pos_lst = []
zero_cnt = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == 2:
            virus_pos_lst.append((r, c))
        if arr[r][c] == 0:
            zero_cnt += 1

# 벽 세우기 시작
backtrack(0, 0)

# (바이러스 퍼지기 전 0 개수) - (바이러스 최소로 퍼졌을 때의 퍼진 칸 개수) - (새로 세워진 벽 3개) 
print(zero_cnt - spread_min - 3)