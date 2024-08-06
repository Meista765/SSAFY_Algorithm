import sys; sys.stdin = open('4836.txt')

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]

    ans = 0
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                arr[r][c] += color
                if arr[r][c] == 3:
                    ans += 1

    print(f'#{tc} {ans}')