# 나무 베기
import sys
from itertools import combinations
from collections import deque
from copy import deepcopy
sys.stdin = open('C:/Users/82108/Downloads/sample_input.txt', 'r')

def dir_change_cnt(origin_dir, goal_dir):
    # 2번 방향 바꿔야하는 경우
    if abs(origin_dir - goal_dir) == 2:
        return 2
    elif origin_dir == goal_dir:
        return 0
    else:
        return 1
    

def BFS(tmp_arr):
    global min_dist
    # 방향 0, 1, 2, 3 => 상, 우, 하, 좌
    # 시작 행, 시작 열, 카운트, 현재 방향
    queue = deque([(start_r, start_c, 0, 0)])
    
    while queue:
        r, c, cnt, origin_dir = queue.popleft()
        
        if tmp_arr[r][c] == 'Y':
            min_dist = min(min_dist, cnt)
            continue
        
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            
            if 0 <= nr < N and 0 <= nc < N and tmp_arr[nr][nc] != 'T' and not visited[nr][nc]:
                visited[nr][nc] = 1
                # 방향 옮기는 카운트 구해보자
                # 상
                if r - nr == 1 and c - nc == 0:
                    goal_dir = 0
                # 우
                elif r - nr == 0 and c - nc == -1:
                    goal_dir = 1
                # 하
                elif r - nr == -1 and c - nc == 0:
                    goal_dir = 2
                # 좌
                elif r - nr == 0 and c - nc == 1:
                    goal_dir = 3
                    
                dir_cnt = dir_change_cnt(origin_dir, goal_dir)
                queue.append((nr, nc, cnt+dir_cnt+1, goal_dir))
        

T = int(input())
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    min_dist = N*N
    
    # RC카의 현재 위치, 나무 좌표 구하기
    start_r = start_c = 0
    tree_pos_lst = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'X':
                start_r, start_c = r, c
            elif arr[r][c] == 'T':
                tree_pos_lst.append((r, c))
    
    # 나무 K개 벤 모든 경우의 수 구하기
    for K_tree in combinations(tree_pos_lst, K):
        visited = [[0] * N for _ in range(N)]
        tmp_arr = deepcopy(arr)
        for tree in K_tree:
            tmp_arr[tree[0]][tree[1]] = 'G'
        BFS(tmp_arr)
    
    if min_dist == N*N:    # min_dist가 그대로라면 (목적지에 도달 불가하다면)
        print(f'#{tc}', -1)
    else:
        print(f'#{tc}', min_dist)
