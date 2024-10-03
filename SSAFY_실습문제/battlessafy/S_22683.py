import sys

sys.stdin = open('input.txt')
from collections import deque


def find_start():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                return (i,j)

def find_end()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'Y':
                return (i,j)

'''
만약 k가 더 크다면 k가 큰걸로 덮어씌운다.
'''

def dijkstra(s,cur_direction):
    q = deque()
    q.append([s, cur_direction, K])
    d[s[0]][s[1]][0] = 0
    arr[s[0]][s[1]] = 'G'

    while q:
        v, cur_direction, k = q.popleft()
        for l in range(4):
            nr = v[0] + dr[l]
            nc = v[1] + dc[l]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 'G':
                    if cur_direction == l:
                        if d[nr][nc][0] > d[v[0]][v[1]][0]+1:
                            d[nr][nc][0] = d[v[0]][v[1]][0]+1

                        elif d[nr][nc][0] == d[v[0]][v[1]][0]+1 and d[nr][nc][1] > d[v[0]][v[1]][1]:
                            d[nr][nc][1] = d[v[0]][v[1]][1]
                    elif abs(cur_direction-l) == 2:
                        if d[nr][nc][0] > d[v[0]][v[1]][0]+3:
                            d[nr][nc][0] = d[v[0]][v[1]][0] + 3
                        elif d[nr][nc][0] == d[v[0]][v[1]][0]+3 and d[nr][nc][1] > d[v[0]][v[1]][1]:
                            d[nr][nc][1] = d[v[0]][v[1]][1]
                    elif abs(cur_direction-l) == 1:
                        if d[nr][nc][0] > d[v[0]][v[1]][0]+2:
                            d[nr][nc][0] = d[v[0]][v[1]][0] + 2
                        elif d[nr][nc][0] == d[v[0]][v[1]][0]+2 and d[nr][nc][1] > d[v[0]][v[1]][1]:
                            d[nr][nc][1] = d[v[0]][v[1]][1]
                # 지나갈 수 없는 곳인데 벨 수 있는 기회가 아직 남아있다면...
                elif arr[nr][nc] == 'T' and d[nr][nc][1] != 0:
                    if cur_direction == l:
                        if d[nr][nc][0] > d[v[0]][v[1]][0]+1:
                            d[nr][nc][0] = d[v[0]][v[1]][0]+1
                            d[nr][nc][1] -= 1
                        elif d[nr][nc][0] == d[v[0]][v[1]][0]+1 and d[nr][nc][1] > d[v[0]][v[1]][1]:
                            d[nr][nc][1] = d[v[0]][v[1]][1]
                            d[nr][nc][1] -= 1
                    elif abs(cur_direction-l) == 2:
                        if d[nr][nc][0] > d[v[0]][v[1]][0]+3:
                            d[nr][nc][0] = d[v[0]][v[1]][0] + 3
                        elif d[nr][nc][0] == d[v[0]][v[1]][0]+3 and d[nr][nc][1] > d[v[0]][v[1]][1]:
                            d[nr][nc][1] = d[v[0]][v[1]][1]
                            d[nr][nc][1] -= 1
                    elif abs(cur_direction-l) == 1:
                        if d[nr][nc][0] > d[v[0]][v[1]][0]+2:
                            d[nr][nc][0] = d[v[0]][v[1]][0] + 2
                        elif d[nr][nc][0] == d[v[0]][v[1]][0]+2 and d[nr][nc][1] > d[v[0]][v[1]][1]:
                            d[nr][nc][1] = d[v[0]][v[1]][1]
                            d[nr][nc][1] -= 1






T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    # d = [[float('inf')] * N for _ in range(N)]  # 최소 조작을 나타내는 배열
    d = [[[float('inf'), K] for _ in range(N)] for _ in range(N)]
    # 상좌하우
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]

    # 위: 0, 왼쪽:1, 아래:3, 오른쪽: 4
    cur_direction = 0

    start = find_start()  # 출발지점
    end = find_end()      # 도착지점

    dijkstra(start,cur_direction,)