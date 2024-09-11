import sys
sys.stdin = open('input.txt')
from heapq import heappop, heappush

def dijkstra(s):
    hq = [(0,s)]
    D[0][0] = 0

    while hq:
        d, v = heappop(hq)
        if v == (N-1,N-1):
            return

        if visited[v[0]][v[1]]:
            continue
        visited[v[0]][v[1]] = 1             # 방문표시
        for k in range(4):
            nr = v[0] + dr[k]
            nc = v[1] + dc[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                diff = arr[nr][nc] - arr[v[0]][v[1]]
                if diff <= 0:
                    diff = 0

                if D[nr][nc] > d + 1 + diff:
                    D[nr][nc] =  d + 1 + diff
                    heappush(hq,(D[nr][nc], (nr,nc)))



T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    D = [[float('inf')] * N for _ in range(N)]

    visited = [[0] * N for _ in range(N)]

    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    start = (0,0)
    dijkstra(start)
    print(f'#{test_case} {D[N-1][N-1]}')
