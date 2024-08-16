N = 7
arr = [[0] * N for _ in range(N)]
r = c = 2

# ------------------------
# 반복문을 이용해서 (r, c)에서 오른쪽 직선 방향의 열값 생성
arr[r][c] = '*'
for i in range(c + 1, N):
    arr[r][i] = '-'

for i in range(c - 1, -1, -1):
    arr[r][i] = '-'

for i in range(r - 1, -1, -1):
    arr[i][c] = '|'

for i in range(1, N):
    nr = r + i
    if nr >= N:
        break
    arr[nr][c] = '|'
    print(nr)


# ------------------------
for line in arr:
    print(*line)