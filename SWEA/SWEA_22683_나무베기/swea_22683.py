import sys
sys.stdin = open('sample_input.txt', 'r')
from collections import deque

T = int(input())

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    field = [list(input()) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if field[r][c] == 'X':
                start = (r, c)
            elif field[r][c] == 'Y':
                goal = (r, c)

    start_r, start_c = start
    q = deque([start_r, start_c, K, 3])
    
    visited = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    visited[r][c][K] = 1
    
