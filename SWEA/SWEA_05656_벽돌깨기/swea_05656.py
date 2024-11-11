import sys
sys.stdin = open('sample_input.txt', 'r')
from itertools import product

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 벽돌 깨는 함수(재귀)
def blocks(r, c, value):    # 깨질 벽돌 좌표, 벽돌 번호
    global copy

    copy[r][c] = 0
    if value == 1:
        return
    else:
        for d in range(4):
            for m in range(1, value):
                nr = r + m * dr[d]
                nc = c + m * dc[d]
                if (0 <= nr < H) and (0 <= nc < W):
                    blocks(nr, nc, copy[nr][nc])
    
def reconstruct():
    global copy

for tc in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())

    # 원본
    field = [list(map(int, input().split())) for _ in range(H)]
    # 복사본
    copy = [[0] * W for _ in range(H)]

    for r in range(H):
        for c in range(W):
            copy[r][c] = field[r][c]

    # 구슬 떨어트리는 순서 조합(cartesian product)
    order = product(list(range(W)), repeat=N)





    