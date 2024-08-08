import sys; sys.stdin = open('2005.txt', 'r')

memo = [[0] * 100 for _ in range(100)]
for n in range(10):
    for r in range(n+1):
        if r == 0 or n == r:
            memo[n][r] = 1
        else:
            memo[n][r] = memo[n-1][r-1] + memo[n-1][r]

for tc in range(1, int(input()) + 1):
    N = int(input())
    print(f'#{tc}')
    for i in range(N):
        print(*memo[i][:i+1])
