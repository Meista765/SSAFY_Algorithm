dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
dir = '-|-|'
N = 7
arr = [[0] * N for _ in range(N)]
r, c = 5, 6
# ------------------------
# 반복문을 이용해서 (r, c)에서 상하좌우 직선방향
arr[r][c] = '*'
for i in range(4): # 네방향에 대해
    for j in range(1, N):
        nr = r + dr[i]*j
        nc = c + dc[i]*j
        if not(0 <= nr < N and 0 <= nc < N):
            break
        arr[nr][nc] = '-'


# ------------------------
for line in arr:
    print(*line)