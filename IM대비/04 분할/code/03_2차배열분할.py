# 2차 배열 4분할
N = 5
arr = [[0] * N for _ in range(N)]
def print_arr():
    for line in arr:
        print(*line)
    print('---------------')

def clear_arr():
    arr = [[0] * N for _ in range(N)]

def set_area(sr, sc, er, ec, val):
    for r in range(sr, er):
        for c in range(sc, ec):
            arr[r][c] = val

for i in range(1, N):
    for j in range(1, N):
        # 1. 좌상단:(0, 0) -> 우하단:(i-1, j-1)
        # r -> range(0, i), c -> range(0, j)
        set_area(0, 0, i, j, 1)
        # 2. (0, j) -> (i-1, N-1)
        set_area(0, j, i, N, 2)
        # 3. (i, 0) -> (N-1, j-1)
        set_area(i, 0, N, j, 3)
        # 4. (i, j) -> (N-1, N-1)
        set_area(i, j, N, N, 4)

        print_arr()
        clear_arr()