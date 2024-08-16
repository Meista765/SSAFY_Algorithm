N = 5
arr = [[0] * N for _ in range(N)]

# 기준점 (r, c)
r = c = 2
arr[r][c] = '*'
# # 상
# arr[r + -1][c + 0] = 1
# # 우
# arr[r + 0][c + 1] = 2
# # 하
# arr[r + 1][c + 0] = 3
# # 좌
# arr[r + 0][c + -1] = 4

r, c = 0, N-1
arr[r][c] = '*'
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    if 0 <= nr < N and 0 <= nc < N:
        arr[nr][nc] = i + 1

# -------------------------------
for line in arr:
    print(*line)