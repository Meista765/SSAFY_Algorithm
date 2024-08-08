import sys; sys.stdin = open('4869.txt', 'r')

memo = [0] * 101

for tc in range(1, int(input()) + 1):
    N = int(input())

    def paper(n):
        if n == 1: return 1
        if n == 2: return 3

        if memo[n]: return memo[n]

        memo[n] = paper(n-1) + paper(n-2)*2

        return memo[n]

    print(paper(N//10))
    