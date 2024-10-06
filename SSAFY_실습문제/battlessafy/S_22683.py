import sys
sys.stdin = open('input.txt')
from heapq import heappush, heappop

# 시작점 찾기
def find_start():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                return (i,j)
# 도착점 찾기
def find_end():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'Y':
                return (i,j)

# 상우하좌
dxy = ((0, -1), (1, 0), (0, 1), (-1, 0))

def dijkstra():
    cost, cut, direction, r, c, cnt = 0, 0, 0, sr, sc, 1
    hq = [(cost, cut, direction, r, c, cnt)]
    visited[cut][sr][sc] = 1                        # 방문 표시
    d[cut][sr][sc] = cost

    while hq:
        cost, cut, direction, r, c, cnt = heappop(hq)

        if r == er and c == ec:
            return cost

        r_dir = (direction + 1) % 4
        l_dir = (direction - 1) % 4
        d_dir = (direction + 2) % 4

        for k in (direction, r_dir, l_dir, d_dir):
            n_cost = cost + 1
            if k == r_dir or k == l_dir:
                n_cost += 1
            elif k == d_dir:
                n_cost += 2

            nr = r + dr[k]
            nc = c + dc[k]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            # 나무를 자르는 경우
            if arr[nr][nc] == 'T' and cut < K and visited[cut+1][nr][nc] == 0 and d[cut+1][nr][nc] > n_cost:
                d[cut+1][nr][nc] = n_cost
                visited[cut+1][nr][nc] = cnt+1
                heappush(hq, (n_cost, cut+1, k, nr, nc, cnt+1))
            # 나무를 안자르는 경우
            if arr[nr][nc] != 'T' and visited[cut][nr][nc] == 0 and d[cut][nr][nc] > n_cost:
                d[cut][nr][nc] = n_cost
                visited[cut][nr][nc] = cnt+1
                heappush(hq, (n_cost, cut, k, nr, nc, cnt+1))
    return -1

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # 상좌하우
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]

    sr, sc = find_start()  # 출발지점
    er, ec = find_end()      # 도착지점

    d = [[[float('inf')] * N for _ in range(N)] for _ in range(K + 1)]         # 거리 정보
    visited = [[[0] * N for _ in range(N)] for _ in range(K + 1)]   # 방문 정보

    answer = dijkstra()
    for i in range(K + 1):
        print(i)
        for j in range(N):
            print(*d[i][j])
        print('===============')

    print(f'#{test_case} {answer}')

