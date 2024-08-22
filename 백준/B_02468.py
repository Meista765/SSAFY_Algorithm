# import sys
# sys.stdin = open('input.txt')
from collections import deque

def bfs(s,rain):
    
    q = deque()
    q.append(s)
    visited[s[0]][s[1]] =1
    
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        v = q.popleft()
        for k in range(4):
            nr = v[0] + dr[k]
            nc = v[1] + dc[k]

            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] > rain and visited[nr][nc] != 1: 
                q.append((nr,nc))                                                      
                visited[nr][nc] = 1


N = int(input())
arr = [[] for _ in range(N)]
max_h =0    # 건물 높이의 최대 값

for i in range(N):
    lst = list(map(int,input().split()))
    max_h = max(0,*lst)
    arr[i] = lst




max_cnt = float('-inf')

for rain in range(max_h+1):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > rain and visited[i][j] != 1:
                bfs((i,j),rain)
                cnt += 1
    max_cnt = max(cnt,max_cnt)            
            

print(max_cnt)