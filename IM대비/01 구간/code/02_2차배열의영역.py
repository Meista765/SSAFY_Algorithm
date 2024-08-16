# 2차배열 내부의 사각영역

N = 10
arr = [[0] * N for _ in range(N)]   # 10 by 10 matrix

# 1. 좌상단 (3, 3), 우하단 (6, 7)
sr, sc = 3, 3
er, ec = 6, 7
for r in range(sr, er + 1):
    for c in range(sc, ec + 1):
        arr[r][c] = 1

for line in arr:
    print(*line)


print('--------------------')
# 2. 좌상단 (3, 3), 높이 = 4, 너비 = 5
arr = [[0] * N for _ in range(N)]
N = 4
M = 5
for r in range(sr, sr + N):
    for c in range(sc, sc + M):
        arr[r][c] = 1

for line in arr:
    print(*line)
