dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N = 7
arr = [[0] * N for _ in range(N)]

K = 3
r = c = 2

# ------------------------
# 반복문을 이용해서 (r, c)에서 상하좌우 K거리 직선방향
arr[r][c] = '*'
for i in range(4): # 네방향에 대해
    for j in range(1, K + 1): # <-- 거리
        nr = r + dr[i]*j
        nc = c + dc[i]*j
        if not(0 <= nr < N and 0 <= nc < N):
            break
        arr[nr][nc] = '-'


# ------------------------
for line in arr:
    print(*line)

