import sys; sys.stdin = open('4869.txt', 'r')

memo = [0] * 101
memo[1], memo[2] = 1, 3
for i in range(3, 101):
    memo[i] = memo[i - 1] + memo[i - 2]*2

for tc in range(1, int(input()) + 1):
    N = int(input())
    print(memo[N//10])
    