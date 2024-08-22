import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(start):
    r = start[0]
    c = start[1]

    houses[r][c] = 0
    q = deque()
    q.append((r, c))
    cnt = 1
    while q:
        row_col = q.popleft()
        r = row_col[0]
        c = row_col[1]
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if (0 <= nr < N) and (0 <= nc < N) and houses[nr][nc] == 1:
                houses[nr][nc] = 0
                q.append((nr, nc))
                cnt+=1
    return cnt

N = int(input())

houses = [list(map(int, list(input()))) for _ in range(N)]

# 우 하 좌 상
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

ans_list = []

for r in range(N):
    for c in range(N):
        if houses[r][c] !=0:
            param = (r, c)
            ans_list.append(bfs(param))

# 정렬
ans_list = sorted(ans_list)
# 단지 수
print(len(ans_list))
# 단지 별 세대 수
for num in ans_list:
    print(num)