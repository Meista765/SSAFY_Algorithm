import sys; sys.stdin = open('1210.txt', 'r')


def find_start_point(ladder, sr, sc):
    r, c = sr, sc
    while r > 0:
        ladder[r][c] = 0
        if c - 1 >= 0 and ladder[r][c - 1] == 1:
            c -= 1
        elif c + 1 < 100 and ladder[r][c + 1] == 1:
            c += 1
        else:
            r -= 1
    return c

for tc in range(1, 11):
    tc_num = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 도착점을 찾아서
    r = c = 0
    for i in range(100):
        if ladder[99][i] == 2:
            r, c = 99, i
            break

    ans = find_start_point(ladder, r, c)

    print(f'#{tc} {ans}')
