# f(n) = f(n-1) + 2*f(n-2)

def f(n):
    global memo
    if n >= 2 and memo[n] == 0:
        memo[n] = f(n-1) + 2*f(n-2)
    return memo[n]
T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    n = int(N / 10)

    memo = [0] * (n+1)
    memo[1] = 1
    memo[2] = 3
    result = f(n)
    print(f'#{test_case} {result}')