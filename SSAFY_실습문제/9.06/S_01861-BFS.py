import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(i,j):
    q = deque()
    q.append((i,j))
    cnt = 1         # 방 이동 횟수

    while q:
        v = q.popleft()
        for k in range(4):
            nr = v[0] + dr[k]
            nc = v[1] + dc[k]
            if 0 <= nr < N and 0 <= nc < N and arr[v[0]][v[1]]+1 == arr[nr][nc]:    # 현재 위치보다 정확히 1 크면 이동 가능
                q.append((nr, nc))
                cnt += 1
    return cnt


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    max_cnt = 1
    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            result = bfs(i, j)
            if result > max_cnt:
                max_cnt = result
                x, y = i, j
            elif result == max_cnt and arr[x][y] > arr[i][j]:   # 같을 때 더 작은 값이 정
                x, y = i, j


    print(f'#{test_case} {arr[x][y]} {max_cnt}')


