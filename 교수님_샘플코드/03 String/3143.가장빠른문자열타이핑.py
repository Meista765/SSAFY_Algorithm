import sys; sys.stdin = open('3143.txt', 'r')

for tc in range(1, int(input()) + 1):
    t, p = input().split()
    n, m = len(t), len(p)
    i = j = 0
    cnt = 0
    while i < n:
        if t[i] != p[j]:
            i = i - j
            j = -1

        i, j = i + 1, j + 1
        if j == m:
            cnt += 1
            j = 0
    print(f'#{tc} {n - (cnt*m) + cnt}')