import sys; sys.stdin = open("4864.txt", "r")


T = int(input())

for tc in range(1, T + 1):
    p = input()
    t = input()
    n, m = len(t), len(p)

    ans = 0
    for i in range(n-m + 1):
        for j in range(m):
            if p[j] != t[i + j]:
                break
        else:
            ans = 1
            break
    print(f'#{tc} {ans}')