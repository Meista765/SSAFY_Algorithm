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
    global min_cnt
    # 시작 행, 시작 열, 카운트, 현재 방향
    queue = deque([(start_r, start_c, 0, 0)])
    visited = [[0] * N for _ in range(N)]       # 방문리스트 초기화
    
    while queue:
        r, c, cnt, origin_dir = queue.popleft()
        visited[r][c] = 1       # 방문 표시
        
        # 종료조건: 목적지에 도달하면 최소 카운트 갱신 후 종료
        if tmp_arr[r][c] == 'Y':
            min_cnt = min(min_cnt, cnt)
            return
        
        for k in range(4):      # 방향 0, 1, 2, 3 => 상, 우, 하, 좌
            nr = r + dr[k]
            nc = c + dc[k]
            
            if 0 <= nr < N and 0 <= nc < N and tmp_arr[nr][nc] != 'T' and not visited[nr][nc]:
                goal_dir = k      # k가 곧 목표 방향이 됨
                dir_cnt = dir_change_cnt(origin_dir, goal_dir)
                queue.append((nr, nc, cnt+dir_cnt+1, goal_dir))
        

T = int(input())
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]  # 상, 우, 하, 좌
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    min_cnt = N*N
    
    # RC카의 현재 위치, 나무 좌표 구하기
    start_r = start_c = 0
    tree_pos_lst = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'T':
                tree_pos_lst.append((r, c))
            elif arr[r][c] == 'X':
                start_r, start_c = r, c
    
    # 존재하는 나무가 K개보다 적을 경우 -> K를 존재하는 나무 개수로 설정
    K = min(K, len(tree_pos_lst))  
    
    # 나무가 없는 경우 바로 BFS 실행
    if K == 0:
        BFS(arr)
    # 나무가 하나 이상 있는 경우
    else:
        # 나무 K개 벤 모든 경우의 수 구하기
        for trees in combinations(tree_pos_lst, K):
            tmp_arr = deepcopy(arr)
            for tree in trees:
                tmp_arr[tree[0]][tree[1]] = 'G'
            BFS(tmp_arr)
    
    if min_cnt == N*N:    # min_cnt가 그대로라면 (목적지에 도달 불가하다면)
        print(f'#{tc}', -1)
    else:
        print(f'#{tc}', min_cnt)