import sys; sys.stdin = open("4864.txt", "r")


T = int(input())

for tc in range(1, T + 1):
    p = input()
    t = input()
    n, m = len(t), len(p)

    ans = 0
    i = j = 0
    while j < m and i < n:
        if t[i] == p[j]:
            i, j = i + 1, j + 1
        else:
            i = i - j + 1
            j = 0
    if j == m:
        ans = 1
    print(f'#{tc} {ans}')