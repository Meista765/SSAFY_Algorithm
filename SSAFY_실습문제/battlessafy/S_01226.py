import sys
sys.stdin = open('input.txt')
from collections import deque

def find_start():
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                return (i,j)



def bfs(start):
    q = deque()
    q.append(start)
    visited = [[0] * 16 for _ in range(16)]
    visited[start[0]][start[1]] = 1         # 방문표시

    while q:
        v = q.popleft()
        if arr[v[0]][v[1]] == 3:
            return 1
        for k in range(4):
            nr = v[0] + dr[k]
            nc = v[1] + dc[k]
            if 0 <= nr < 16 and 0 <= nc < 16 and visited[nr][nc] == 0 and arr[nr][nc] != 1:
                visited[nr][nc] = 1
                q.append((nr,nc))
    return 0



for test_case in range(1,11):
    tc = int(input())
    arr = [list(map(int,list(input()))) for _ in range(16)]
    start = find_start()

    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    answer = bfs(start)
    print(f'#{test_case} {answer}')