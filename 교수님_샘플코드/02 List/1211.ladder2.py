import sys; sys.stdin = open('1211.txt', 'r')

# 위에서 아래 방향으로
def find_start_point(ladder, sr, sc):
    r, c = sr, sc
    dist = 0
    while r < 100:
        if c - 1 >= 0 and ladder[r][c - 1] == 1:
            while c - 1 >= 0 and ladder[r][c - 1] == 1:
                c -= 1
                dist += 1
        elif c + 1 < 100 and ladder[r][c + 1] == 1:
            while c + 1 < 100 and ladder[r][c + 1] == 1:
                c += 1
                dist += 1
        r += 1
    return dist

for tc in range(1, 11):
    tc_num = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    min_dist = 10000
    for c in range(100):
        if ladder[0][c] == 0:
            continue

        dist = find_start_point(ladder, 0, c)

        if min_dist >= dist:
            min_dist = dist
            ans = c
    print(f'#{tc} {ans}')
